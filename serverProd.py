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
import psycopg2
import csv


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__, static_folder='dist')
app.secret_key = env.get("APP_SECRET_KEY")

CORS(app)

uidirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dist')

import csv

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
            writer = csv.DictWriter(file, fieldnames=['ngrok_email', 'ngrok_name'])
            writer.writerow({'ngrok_email': user_email, 'ngrok_name': user_name, 'new': True})
        

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
                    return jsonify({'form_first_name': row['form_first_name'],'ngrok_email': ngrok_email, 'form_first_surname': row['form_first_surname']})
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

    
