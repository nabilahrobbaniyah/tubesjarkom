import socket
import struct

GROUP="239.255.1.1"
PORT=5000
BUFFER=1024

# GANTI DENGAN IP RECEIVER
LOCAL_IP="192.168.137.1"

sock=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
    socket.IPPROTO_UDP
)

sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

sock.bind(
    ("0.0.0.0",PORT)
)

# JOIN GROUP SECARA EKSPLISIT
mreq=(
    socket.inet_aton(GROUP)
    +
    socket.inet_aton(LOCAL_IP)
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)

print("Receiver multicast aktif")

file=None

while True:

    data,addr=sock.recvfrom(BUFFER)

    if data.startswith(
        b"FILE:"
    ):

        filename=data[5:].decode()

        file=open(
            "received_"+filename,
            "wb"
        )

        print(
            "Mulai:",
            filename
        )

    elif data==b"EOF":

        if file:
            file.close()

        print(
            "Transfer selesai"
        )

    else:

        if file:
            file.write(data)
