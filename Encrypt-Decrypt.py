from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open("encryption_key.txt", 'wb')
file.write(key)
file.close()

WiFi_pass = "information-wifi.txt"

encrypted_file = [WiFi_pass]
c = 0


for decrypting_files in encrypted_file:
    with open(encrypted_file[c], 'rb') as f:
        data = f.read()
