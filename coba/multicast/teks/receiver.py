import socket
import struct

GROUP="239.255.1.1"
PORT=5000

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
    ("",PORT)
)

mreq=struct.pack(
    "4s4s",
    socket.inet_aton(GROUP),
    socket.inet_aton(LOCAL_IP)
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)

print("join")

while True:

    data,addr=sock.recvfrom(1024)

    print(
        data.decode()
    )
