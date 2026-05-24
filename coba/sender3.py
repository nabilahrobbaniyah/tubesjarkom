import socket
import struct

GROUP = "224.1.1.1"
PORT = 5000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
    socket.IPPROTO_UDP
)

# ttl hanya LAN
ttl = struct.pack("b",1)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    ttl
)

print("Sender aktif")

while True:

    pesan=input("\nPesan: ")

    if pesan=="exit":
        break

    sock.sendto(
        pesan.encode(),
        (GROUP,PORT)
    )

    print("Terkirim")
