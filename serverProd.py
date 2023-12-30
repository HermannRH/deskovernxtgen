from flask import Flask, request, send_from_directory, redirect, render_template, session, url_for
from flask_cors import CORS
import os
from os import environ as env
from werkzeug.utils import secure_filename
from flask import jsonify
import json
import pandas as pd
from urllib.parse import quote_plus, urlencode
from dotenv import find_dotenv, load_dotenv
import ast
import re
import logging
from logging.handlers import RotatingFileHandler
import csv
import base64
import random


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__, static_folder='dist')
app.secret_key = env.get("APP_SECRET_KEY")

CORS(app)

uidirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dist')



def save_image(base64_string, name_prefix):
    # Extract the base64 part by splitting the string
    header, base64_str = base64_string.split(',', 1)
    
    # Check if the directory 'photos' exists, if not create one
    os.makedirs('photos', exist_ok=True)
    
    # Generate a random 4 digit number and create the image filename
    random_number = random.randint(1000, 9999)
    filename = f"{name_prefix}_{random_number}.png"
    filepath = os.path.join('photos', filename)
    
    # Decode the base64 string and write the image to a file
    with open(filepath, 'wb') as f:
        f.write(base64.b64decode(base64_str))
        
    return filename


@app.before_request
def before_request():
    user_email = request.headers.get('Ngrok-Auth-User-Email')
    user_name = request.headers.get('Ngrok-Auth-User-Name')
    new = False

    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ngrok_email'] == user_email:
                new = False
                break
        else:
            new = True

    if new:
        # Print the column names of the csv
        with open('users.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ngrok_email', 'ngrok_name', 'new'])
            writer.writerow({'ngrok_email': user_email, 'ngrok_name': user_name, 'new': True})



@app.route('/api/form', methods=['POST'])
def handle_form():
    form_data = request.json
    image_filename = save_image(form_data['image'], form_data['name'].split(' ')[0])
    csv_file_path = 'users.csv'
    user_email = request.headers.get('Ngrok-Auth-User-Email')

    # Read the CSV file into a list of dictionaries
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Update the relevant dictionary
    for row in data:
        if row['ngrok_email'] == user_email:
            row.update({
                'ngrok_name': form_data['name'],
                'new': 'False',
                'form_first_name': form_data['name'],
                'form_age': form_data['age'],
                'form_blood': form_data['bloodType'],
                'form_birthday': form_data['birthDate'],
                'form_email': form_data['email'],
                'form_phone': form_data['phone'],
                'form_loc': form_data['address'],
                'form_insura': form_data['insuranceCompany'],
                'form_intype': form_data['insuranceType'],
                'img_name': image_filename
            })

    # Write the list back to the CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return jsonify({'message': 'Form submitted successfully', 'image_filename': image_filename}), 200

@app.route('/api/info')
def get_info():
    ngrok_email = request.headers.get('Ngrok-Auth-User-Email')
    ngrok_name = request.headers.get('Ngrok-Auth-User-Name')
    # Check the user csv for the email, and retrieve the column "new" if it is true send back a "new" flag, if not return the id column on the csv
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ngrok_email'] == ngrok_email:
                if row['new'] == 'True':
                    return jsonify({'new': True})
                else:
                    return jsonify({'form_first_name': row['form_first_name'],'ngrok_email': ngrok_email})
        else:
            return jsonify({'new': True})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    file_to_serve = os.path.join(app.static_folder, path)  # Changed here
    if path != "" and os.path.exists(file_to_serve):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
    

if __name__ == "__main__":
    print("Starting the application")
    app.run(port=8080, debug=True)

    

