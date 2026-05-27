import socket

PORT = 5000

INTERFACE = "192.168.137.100"

BROADCAST = "192.168.137.255"

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

sock.bind(
    (INTERFACE,0)
)

sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_BROADCAST,
    1
)

while True:

    msg=input()

    sock.sendto(
        msg.encode(),
        (BROADCAST,PORT)
    )

    print("terkirim")
