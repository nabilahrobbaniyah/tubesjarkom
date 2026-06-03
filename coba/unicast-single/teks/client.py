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

print("Terhubung")

while True:

    pesan = input(
        "\nMasukkan pesan: "
    )

    if pesan.lower() == "exit":
        break

    client.send(
        pesan.encode()
    )

client.close()
