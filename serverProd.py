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
from logging.handlers import RotatingFileHandler
import csv
import base64
import random
from datetime import datetime, timedelta
from flask import abort
from flask import send_file
import io
import shutil
import zipfile


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__, static_folder='dist')
app.secret_key = env.get("APP_SECRET_KEY")

CORS(app)

uidirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dist')



def save_image(base64_string, name_prefix):
    # If no image is provided, return "Sin Fotografia"
    if not base64_string:
        return "Sin Fotografia"

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


@app.route('/api/form', methods=['POST'])
def handle_form():
    form_data = request.json
    image_filename = save_image(form_data['image'], form_data['name'].split(' ')[0])
    csv_file_path = 'users.csv'
    ip = request.remote_addr


    # Read the CSV file into a list of dictionaries
    with open(csv_file_path,encoding='latin1', mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    row_updated = False 
    now = datetime.now()

    # Update the relevant dictionary
    for row in data:
        # Parse 'Hora_Registro' into a datetime object
        try:
            hora_registro = datetime.strptime(row['Hora_Registro'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            continue

        # Get the current time
        if row['Numero_Tarjeta'] == form_data['folioCheckInicial'] and (now - hora_registro).total_seconds() <= 3600:
            row.update({
            'Nombre_Completo': form_data['name'],
            'Edad': form_data['age'],
            'Fecha_Nacimiento': form_data['birthDate'],
            'Tipo_Sangre': form_data['bloodType'],
            'Correo_Electronico': form_data['email'],
            'Telefono': form_data['phone'],
            'Direccion': form_data['address'],
            'Tipo_Seguro': form_data['insuranceType'],
            'Nombre_Aseguradora': form_data['insuranceCompany'],
            'Numero_Tarjeta': form_data['folioCheckInicial'],  
            'Acepta_Terminos_Condiciones': form_data['termsConditions'],  # Assuming a field for terms and conditions acceptance
            'Fotografia': form_data['image'],
            'Nombre_Fotografia': image_filename,
            'IP': ip,
        })
            row_updated = True
            break

    if not row_updated:
    # Append a new row
        data.append({
            'Nombre_Completo': form_data['name'],
            'Edad': form_data['age'],
            'Fecha_Nacimiento': form_data['birthDate'],
            'Tipo_Sangre': form_data['bloodType'],
            'Correo_Electronico': form_data['email'],
            'Telefono': form_data['phone'],
            'Direccion': form_data['address'],
            'Tipo_Seguro': form_data['insuranceType'],
            'Nombre_Aseguradora': form_data['insuranceCompany'],
            'Numero_Tarjeta': form_data['folioCheckInicial'],  
            'Acepta_Terminos_Condiciones': True,
            'Nombre_Fotografia': image_filename,
            'IP': ip,
            'Hora_Registro': now.strftime('%Y-%m-%d %H:%M:%S'),
        })
            
            
    # Write the list back to the CSV file
    with open(csv_file_path, encoding='latin1', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return jsonify({'message': 'Form submitted successfully', 'image_filename': image_filename}), 200

@app.route('/api/info')
def get_info():
    csv_file_path = 'users.csv'
    unique_Tipo_Seguro = set()
    unique_Nombre_Aseguradora = set()
    unique_Numero_Tarjeta = set()

    # Read and extract the unique values for Tipo_Seguro and Nombre_Aseguradora
    with open(csv_file_path, encoding='latin1', mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        for row in data:
            unique_Tipo_Seguro.add(row['Tipo_Seguro'])
            unique_Nombre_Aseguradora.add(row['Nombre_Aseguradora'])
            unique_Numero_Tarjeta.add(row['Numero_Tarjeta'])
    
    # Convert the sets to lists
    unique_Tipo_Seguro = list(unique_Tipo_Seguro)
    unique_Nombre_Aseguradora = list(unique_Nombre_Aseguradora)
    unique_Numero_Tarjeta = list(unique_Numero_Tarjeta)

    Numero_Tarjeta = request.args.get('folioCheckInicial')
    now = datetime.now()
    hora_registro = now.strftime('%Y-%m-%d %H:%M:%S')
    # Now we will append a new row to the csv, only if the card number is not present in the CSV file
    if Numero_Tarjeta not in unique_Numero_Tarjeta:
        print("Card number not present in the CSV file")
        data.append({
            'Numero_Tarjeta': Numero_Tarjeta,
            'Hora_Registro': hora_registro,
        })

    # Write the list back to the CSV file
    with open(csv_file_path, encoding='latin1', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return jsonify({'unique_Tipo_Seguro': unique_Tipo_Seguro, 'unique_Nombre_Aseguradora': unique_Nombre_Aseguradora}), 200


@app.route('/api/pullmoll')
def pull_moll():
    email = request.args.get('email')
    password = request.args.get('password')
    downloadUserData = request.args.get('downloadUserData')
    downloadImages = request.args.get('downloadImages')
    print(email)
    print(password)
    text = email + password
    if not text == env.get('COMBINATION'):
        print("Wrong password")
        buffer = io.BytesIO()
        
        with zipfile.ZipFile(buffer, 'w') as zipf:
            zipf.writestr('Data.txt', b'd a t a' * 1024 * 1025)
        buffer.seek(0)
        def corrupt_buffer(buffer):
            data = bytearray(buffer.getvalue())
            for i in range(len(data)):
                data[i] = random.randint(0, 255)
            buffer.seek(0)
            buffer.write(data)
            buffer.seek(0)

        corrupt_buffer(buffer)

        return send_file(buffer, as_attachment=True, download_name='data.zip')
    if text == env.get('COMBINATION'):
        print("Correct password")
        in_memory_buffer = io.BytesIO()
        with zipfile.ZipFile(in_memory_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zipf:
            if downloadUserData:
                zipf.write('users.csv', arcname='users.csv')
            if downloadImages:
                for root, dirs, files in os.walk('photos'):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), 'photos'))
        in_memory_buffer.seek(0)
        return send_file(in_memory_buffer, as_attachment=True, download_name='Informacion.zip')





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
    app.run(port=8080, debug=False)

    

