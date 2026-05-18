import socket
import os
import struct

MULTICAST_GROUP = "224.1.1.1"
PORT = 5000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

# TTL multicast
ttl = struct.pack('b', 1)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    ttl
)

filepath = input("Masukkan path file: ")

filename = os.path.basename(filepath)

# Kirim nama file dulu
sock.sendto(
    f"FILENAME:{filename}".encode(),
    (MULTICAST_GROUP, PORT)
)

# Kirim file
with open(filepath, "rb") as file:

    while True:

        data = file.read(4096)

        if not data:
            break

        sock.sendto(data, (MULTICAST_GROUP, PORT))

# Penanda selesai
sock.sendto(
    b"END_FILE",
    (MULTICAST_GROUP, PORT)
)

print("File multicast selesai dikirim")