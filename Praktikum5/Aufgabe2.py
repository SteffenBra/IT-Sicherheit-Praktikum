import base64
import requests

if __name__ == '__main__':

    with open('Praktikum5/c2.dat') as file:        
            base64_code = file.read()
            base64_bytes = base64_code.encode('utf-8')
            ciphertext = base64.b64decode(base64_bytes)

    drucke_text = "                DRUCKE   "
    speichern_text = "                SPEICHERN"

    modified_ciphertext = bytearray(ciphertext)
    for i in range(len(drucke_text)):
        old_ciphertext = modified_ciphertext[i]
        modified_ciphertext[i] ^= ord(speichern_text[i]) ^ ord(drucke_text[i])
        print(speichern_text[i]+" "+str(ord(speichern_text[i]))+"   "+drucke_text[i]+" "+str(ord(drucke_text[i]))+"   "+str(old_ciphertext)+"   "+str(modified_ciphertext[i]))


    modified_ciphertext = base64.b64encode(modified_ciphertext).decode('utf-8')


    print(modified_ciphertext)


    URL = "http://fb02itssebastian.fh-muenster.de:31337"
    HEADERS = {'ciphertext':modified_ciphertext}

    r = requests.get(url = URL, headers= HEADERS)
    
    data = r.content
    print(data)