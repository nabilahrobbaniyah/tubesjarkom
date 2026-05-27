import socket

PORT=5000

sock=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

sock.bind(
    ("0.0.0.0",PORT)
)

print("listen")

while True:

    data,addr=sock.recvfrom(1024)

    print(
        data.decode()
    )
