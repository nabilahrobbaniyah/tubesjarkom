import socket
import struct

GROUP="224.1.1.1"
PORT=5000

LOCAL_IP="192.168.1.11"

sock=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    struct.pack("b",1)
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_IF,
    socket.inet_aton(LOCAL_IP)
)

while True:

    pesan=input("Pesan: ")

    sock.sendto(
        pesan.encode(),
        (GROUP,PORT)
    )
