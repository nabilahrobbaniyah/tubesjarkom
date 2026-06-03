import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(
    (HOST, PORT)
)

server.listen()

print(
    "Server multithread aktif"
)

def handle_client(
    client,
    addr
):

    print(
        f"\nClient masuk {addr}"
    )

    while True:

        try:

            data = client.recv(
                4096
            )

            if not data:
                break

            print(
                f"\n[{addr}]"
            )

            print(
                data.decode()
            )

        except:
            break

    client.close()

    print(
        f"{addr} keluar"
    )

while True:

    client, addr = (
        server.accept()
    )

    thread = (
        threading.Thread(
            target=handle_client,
            args=(
                client,
                addr
            )
        )
    )

    thread.start()
