import socket
import os

# Membuat folder received jika belum ada
if not os.path.exists("received"):
    os.makedirs("received")

# Membuat socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP dan port
server.bind(("0.0.0.0", 5000))

# Listen client
server.listen(1)

print("Server menunggu koneksi...")

# Accept client
client_socket, addr = server.accept()

print(f"Terhubung ke {addr}")

# Menerima nama file
filename = client_socket.recv(1024).decode()

print("Menerima file:", filename)

# Simpan file
filepath = os.path.join("received", filename)

with open(filepath, "wb") as file:

    while True:

        data = client_socket.recv(4096)

        # Jika data habis
        if not data:
            break

        file.write(data)

print("File berhasil diterima")

client_socket.close()
server.close()