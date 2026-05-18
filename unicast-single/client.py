import socket
import os

# Buat socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect ke server
client.connect(("192.168.1.2", 5000))

# Pilih file
filepath = input("Masukkan path file: ")

filename = os.path.basename(filepath)

# Kirim nama file
client.send(filename.encode())

# Delay kecil agar nama file terkirim dulu
import time
time.sleep(1)

# Kirim isi file
with open(filepath, "rb") as file:

    while True:

        data = file.read(4096)

        if not data:
            break

        client.sendall(data)

print("File berhasil dikirim")

client.close()