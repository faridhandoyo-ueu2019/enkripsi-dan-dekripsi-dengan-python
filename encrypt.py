from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

with open('coba.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)
with open('coba.txt.encrypted', 'wb') as f:
    f.write(encrypted)
