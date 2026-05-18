import socket
import threading
import os
import time

# Folder received
if not os.path.exists("received"):
    os.makedirs("received")

# Fungsi handle client
def handle_client(client_socket, addr):

    print(f"Client {addr} terhubung")

    # Terima nama file
    filename = client_socket.recv(1024).decode()

    # Tambahkan timestamp agar unik
    unique_filename = f"{int(time.time())}_{filename}"

    filepath = os.path.join("received", unique_filename)

    with open(filepath, "wb") as file:

        while True:

            data = client_socket.recv(4096)

            if not data:
                break

            file.write(data)

    print(f"File {unique_filename} selesai diterima")

    client_socket.close()

# Socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))

server.listen(5)

print("Server multithread aktif...")

while True:

    client_socket, addr = server.accept()

    # Thread baru
    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, addr)
    )

    thread.start()