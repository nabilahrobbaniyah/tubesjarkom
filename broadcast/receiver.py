import socket

PORT = 5000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

sock.bind(("", PORT))

print("Receiver broadcast aktif...")

file = None

while True:

    data, addr = sock.recvfrom(4096)

    # Nama file
    if data.startswith(b"FILENAME:"):

        filename = data.decode().split(":")[1]

        file = open(f"received_{filename}", "wb")

        print("Menerima:", filename)

    elif data == b"END_FILE":

        if file:
            file.close()

        print("File selesai diterima")

    else:

        if file:
            file.write(data)