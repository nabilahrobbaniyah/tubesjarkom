import socket
import struct

GROUP="239.255.1.1"
PORT=5000

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

while True:

    msg=input()

    sock.sendto(
        msg.encode(),
        (GROUP,PORT)
    )
