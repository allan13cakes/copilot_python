import os
from cryptography.fernet import Fernet

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Read the key from the file
with open('key.key', 'rb') as key_file:
    key = key_file.read()

# Create a Fernet object with the key
cipher = Fernet(key)

# Read the encrypted password from the configuration file
config = {'username': 'jlyq2016@163.com', 'password': 'gAAAAABkxhXXytVoquIGfeAx4WLjOTxZRxZkbBXS67tuoXoz2YRIdbA7BVbahkOqteFgbdjTYjcpM867auwRZt6b6xAJGqqTbQ=='}


# Use the decrypted password in your test code
# print(decrypted_password.decode('utf-8'))  # prints 'mysecretpassword'