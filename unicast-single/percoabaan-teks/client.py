import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(
    ("192.168.1.5",5000)
)

pesan = input(
    "Masukkan teks: "
)

client.send(
    pesan.encode()
)

client.close()
