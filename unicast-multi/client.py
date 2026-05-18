import socket
import os
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.1.2", 5000))

filepath = input("Masukkan path file: ")

filename = os.path.basename(filepath)

# Kirim nama file
client.send(filename.encode())

time.sleep(1)

# Kirim file
with open(filepath, "rb") as file:

    while True:

        data = file.read(4096)

        if not data:
            break

        client.sendall(data)

print("File berhasil dikirim")

client.close()