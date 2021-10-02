from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

with open('coba.txt.encrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)
with open('coba.txt.decrypted', 'wb') as f:
    f.write(encrypted)
