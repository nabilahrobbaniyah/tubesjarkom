import socket

SERVER_IP = "192.168.1.11"

PORT = 5000

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(
    (SERVER_IP, PORT)
)

print(
    "Terhubung"
)

while True:

    msg = input(
        "\nPesan: "
    )

    if msg == "exit":
        break

    client.send(
        msg.encode()
    )

client.close()
