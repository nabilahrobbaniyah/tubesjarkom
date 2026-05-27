import socket

PORT = 5000
BUFFER = 1024

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

sock.bind(
    ("", PORT)
)

print(
    "Receiver broadcast aktif"
)

file = None

while True:

    data, addr = sock.recvfrom(
        BUFFER
    )

    if data.startswith(
        b"FILE:"
    ):

        filename = (
            data.decode()[5:]
        )

        file = open(
            "received_" + filename,
            "wb"
        )

        print(
            "Menerima:",
            filename
        )

    elif data == b"EOF":

        if file:
            file.close()

        print(
            "Selesai"
        )

    else:

        if file:
            file.write(
                data
            )
