from Crypto.Cipher import AES
import hashlib
from os import urandom


text = 'Hello world'.encode('ascii')
secret_key = hashlib.sha256(urandom(16)).digest()
obj = AES.new(secret_key,AES.MODE_EAX)

enc = obj.encrypt(text)
with open("secret.txt","wb") as f:
    f.write(secret_key)
    f.close()
with open("enctext.ppk",'wb') as file:
    file.write(enc)
    file.close()
key = open("secret.txt",'rb').read()
enctext = open("enctext.ppk",'rb').read()
obj2 = AES.new(key,AES.MODE_EAX,nonce=obj.nonce)
plaintext = obj2.decrypt(enctext)
print(plaintext)

