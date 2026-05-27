import socket
import struct
import os
import time

GROUP="239.255.1.1"
PORT=5000
BUFFER=1024

# GANTI DENGAN IP SENDER
LOCAL_IP="192.168.137.1"

sock=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
    socket.IPPROTO_UDP
)

# PAKSA INTERFACE
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_IF,
    socket.inet_aton(LOCAL_IP)
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    struct.pack("b",2)
)

path=input(
    "Masukkan file: "
)

filename=os.path.basename(
    path
)

sock.sendto(
    (
        "FILE:"+filename
    ).encode(),
    (GROUP,PORT)
)

time.sleep(1)

with open(
    path,
    "rb"
) as file:

    while True:

        data=file.read(
            BUFFER
        )

        if not data:
            break

        sock.sendto(
            data,
            (GROUP,PORT)
        )

        time.sleep(
            0.01
        )

sock.sendto(
    b"EOF",
    (GROUP,PORT)
)

print(
    "File terkirim"
)
