import socket
import struct

MULTICAST_GROUP = "224.1.1.1"
PORT = 5000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
    socket.IPPROTO_UDP
)

sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

sock.bind(("", PORT))

mreq = struct.pack(
    "4sl",
    socket.inet_aton(MULTICAST_GROUP),
    socket.INADDR_ANY
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)

print("Receiver multicast aktif...")

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