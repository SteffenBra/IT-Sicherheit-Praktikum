import hashlib
import base64
from Crypto.Cipher import AES

if __name__ == '__main__':

    key = hashlib.sha256("dun2018".encode('utf-8')).digest()[0:16]

    with open('Praktikum5/c1.dat') as file:        
        base64_code = file.read()
        base64_bytes = base64_code.encode('utf-8')
        ciphertext = base64.b64decode(base64_bytes)

    iv = ciphertext[:16]
    encrypted_text = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(encrypted_text)
    print(decrypted_text.decode('utf-8'))
