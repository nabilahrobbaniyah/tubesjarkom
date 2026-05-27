import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(
    (HOST, PORT)
)

server.listen(1)

print("Server aktif")
print("Menunggu client...\n")

client, addr = server.accept()

print(
    "Client terhubung:",
    addr
)

while True:

    data = client.recv(
        4096
    )

    if not data:
        break

    print(
        "\nPesan diterima:"
    )

    print(
        data.decode()
    )

client.close()

server.close()
