import socket
import struct

GROUP = "239.1.1.1"
PORT = 5000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
    socket.IPPROTO_UDP
)

# TTL = hanya LAN
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    struct.pack("b", 2)
)

# aktifkan loopback
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_LOOP,
    1
)

print("Sender aktif")

while True:

    msg = input("Pesan: ")

    sock.sendto(
        msg.encode(),
        (GROUP, PORT)
    )

    print("Terkirim")
