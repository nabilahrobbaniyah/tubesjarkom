import socket

TARGET="192.168.1.14"

sock=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

while True:

    msg=input()

    sock.sendto(
        msg.encode(),
        (TARGET,5000)
    )
