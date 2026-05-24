import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(("0.0.0.0",5000))

server.listen()

print("Menunggu client...")

client, addr = server.accept()

data = client.recv(4096)

print("\nPesan diterima:")
print(data.decode())

client.close()
