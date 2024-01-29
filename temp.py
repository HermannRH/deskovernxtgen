import os
from os import environ as env
from dotenv import find_dotenv, load_dotenv
import bcrypt

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Get the password from the user
password = ""  # replace with the user's password

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))

# Check if the hash between the email and password is equal to the env HASHED_PASSWORD variable
if bcrypt.checkpw(password.encode('utf-8'), env.get('HASHED_PASSWORD').encode('utf-8')):
    print("Correct password")


