import socket
import os

PORT = 5000
BUFFER = 1024

BROADCAST = "192.168.137.255"

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_BROADCAST,
    1
)

path = input(
    "Masukkan file: "
)

filename = os.path.basename(
    path
)

sock.sendto(
    f"FILE:{filename}".encode(),
    (BROADCAST, PORT)
)

with open(
    path,
    "rb"
) as file:

    while True:

        data = file.read(
            BUFFER
        )

        if not data:
            break

        sock.sendto(
            data,
            (BROADCAST, PORT)
        )

sock.sendto(
    b"EOF",
    (BROADCAST, PORT)
)

print(
    "Broadcast selesai"
)
