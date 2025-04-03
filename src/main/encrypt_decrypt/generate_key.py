from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()

# Save the key securely
with open("secret.key","wb") as key_file:
    key_file.write(key)

print("Encryption key generated & saved in .secret file")



