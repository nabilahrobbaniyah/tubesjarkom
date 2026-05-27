import socket
import struct

GROUP="239.255.1.1"
PORT=5000

LOCAL_IP="192.168.137.100"

sock=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
    socket.IPPROTO_UDP
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    struct.pack("b",2)
)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_IF,
    socket.inet_aton(LOCAL_IP)
)

while True:

    msg=input()

    sock.sendto(
        msg.encode(),
        (GROUP,PORT)
    )
