import socket
import os

PORT = 5000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

# Aktifkan broadcast
sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_BROADCAST,
    1
)

filepath = input("Masukkan path file: ")

filename = os.path.basename(filepath)

# Kirim nama file
sock.sendto(
    f"FILENAME:{filename}".encode(),
    ("255.255.255.255", PORT)
)

# Kirim isi file
with open(filepath, "rb") as file:

    while True:

        data = file.read(4096)

        if not data:
            break

        sock.sendto(
            data,
            ("255.255.255.255", PORT)
        )

# Penanda akhir
sock.sendto(
    b"END_FILE",
    ("255.255.255.255", PORT)
)

print("Broadcast selesai")