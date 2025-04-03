import configparser
from cryptography.fernet import Fernet
import os

# Load encryption key
# with open("secret.key","rb") as key_file:
#     key = key_file.read()

key = os.getenv("CONFIG_SECRET_KEY")

if not key:
    raise ValueError("ERROR: CONFIG_SECRET_KEY is not set! Please set it in your environment.")

cipher = Fernet(key.encode())

# Read original config file
config = configparser.ConfigParser()
config.read(r"C:\Users\ashfa\OneDrive\Documents\Reminder Series\src\resources\config.ini")


# Encrypt sensitive fields
config.set("MYSQL_CREDENTIALS", "MYSQL_HOST", cipher.encrypt(config["MYSQL_CREDENTIALS"]["MYSQL_HOST"].encode()).decode())
config.set("MYSQL_CREDENTIALS", "MYSQL_PORT", cipher.encrypt(config["MYSQL_CREDENTIALS"]["MYSQL_PORT"].encode()).decode())
config.set("MYSQL_CREDENTIALS", "MYSQL_USER", cipher.encrypt(config["MYSQL_CREDENTIALS"]["MYSQL_USER"].encode()).decode())
config.set("MYSQL_CREDENTIALS", "MYSQL_PASSWORD", cipher.encrypt(config["MYSQL_CREDENTIALS"]["MYSQL_PASSWORD"].encode()).decode())
config.set("MYSQL_CREDENTIALS", "MYSQL_DATABASE", cipher.encrypt(config["MYSQL_CREDENTIALS"]["MYSQL_DATABASE"].encode()).decode())
config.set("MYSQL_CREDENTIALS", "LOCAL_PORT", cipher.encrypt(config["MYSQL_CREDENTIALS"]["LOCAL_PORT"].encode()).decode())


# Save encrypted fileds
with open("config_encrypted.ini","w") as configfile:
    config.write(configfile)


print("Config file encrypted & saved as 'config_encrypted.ini'")


