import socket
import struct
import os

GROUP = "239.255.1.1"
PORT = 5000
BUFFER = 1024

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
    socket.IPPROTO_UDP
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    struct.pack("b", 2)
)

path = input(
    "Masukkan path file: "
)

filename = os.path.basename(
    path
)

sock.sendto(
    f"FILE:{filename}".encode(),
    (GROUP, PORT)
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
            (GROUP, PORT)
        )

sock.sendto(
    b"EOF",
    (GROUP, PORT)
)

print("File berhasil dikirim")
