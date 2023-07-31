from cryptography.fernet import Fernet
# Generate a new encryption key
key = Fernet.generate_key()

# Store the key in a file (keep this file secure!)
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Encrypt a password
password = b''
cipher = Fernet(key)
encrypted_password = cipher.encrypt(password)

# Store the encrypted password in the configuration file
config = {
    'username': 'myusername',
    'password': encrypted_password.decode('utf-8')
}

print(config)