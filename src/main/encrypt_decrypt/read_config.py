import configparser
from cryptography.fernet import Fernet
import os

# # Load encryption key 
# with open("secret.key","rb") as key_file:
#     key = key_file.read()

key = os.getenv("CONFIG_SECRET_KEY")

if not key:
    raise ValueError("ERROR: CONFIG_SECRET_KEY is not set! Please set it in your environment.")

cipher = Fernet(key.encode())

# Read encrypted config
config = configparser.ConfigParser()
config.read("config_encrypted.ini")

# Function to decrypt values
def decrypt_values(encrypted_value):
    return cipher.decrypt(encrypted_value.encode()).decode()

# Function to return Mysql Credentials
def get_mysql_credentials():
    return {

        "host": decrypt_values(config["MYSQL_CREDENTIALS"]["MYSQL_HOST"]),
        "port": int(decrypt_values(config["MYSQL_CREDENTIALS"]["MYSQL_PORT"])),  # Convert to int
        "user": decrypt_values(config["MYSQL_CREDENTIALS"]["MYSQL_USER"]),
        "password": decrypt_values(config["MYSQL_CREDENTIALS"]["MYSQL_PASSWORD"]),
        "database": decrypt_values(config["MYSQL_CREDENTIALS"]["MYSQL_DATABASE"]),
        "local_port": int(decrypt_values(config["MYSQL_CREDENTIALS"]["LOCAL_PORT"]))  # Convert to int
   
    }






