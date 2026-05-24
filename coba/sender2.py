import socket

PORT=5000

sock=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
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
        ("192.168.137.255",PORT)
    )
