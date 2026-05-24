# multicast
import socket
import struct
import os

# ==========================
# KONFIGURASI
# ==========================

MULTICAST_GROUP = "224.1.1.1"
PORT = 5000

# GANTI DENGAN IP LAPTOP SENDER
LOCAL_IP = "192.168.1.10"

# ==========================
# BUAT SOCKET UDP
# ==========================

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

# TTL = hanya LAN
ttl = struct.pack("b", 1)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    ttl
)

# Tentukan interface jaringan
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_IF,
    socket.inet_aton(LOCAL_IP)
)

print("=== MULTICAST SENDER ===")

# ==========================
# INPUT FILE
# ==========================

filepath = input(
    "Masukkan path file: "
)

filename = os.path.basename(filepath)

# ==========================
# KIRIM NAMA FILE
# ==========================

sock.sendto(
    f"FILENAME:{filename}".encode(),
    (MULTICAST_GROUP, PORT)
)

print("Nama file dikirim")

# ==========================
# KIRIM ISI FILE
# ==========================

with open(filepath, "rb") as file:

    while True:

        data = file.read(1024)

        if not data:
            break

        sock.sendto(
            data,
            (MULTICAST_GROUP, PORT)
        )

# ==========================
# KIRIM PENANDA SELESAI
# ==========================

sock.sendto(
    b"END_FILE",
    (MULTICAST_GROUP, PORT)
)

print("File berhasil dikirim")

sock.close()
