import socket
from time import sleep

server = socket.socket()

port = 8102
server.bind(("", port))

server.listen()
timeout = 30

while True:
    server.settimeout(timeout)
    client, addr = None, None
    try:
        client, addr = server.accept()
    except TimeoutError:
        print(f'Waited {timeout} seconds with no connections.')
        break

    bytes = int(client.recv(1024).decode())
    packet = "a" * bytes
    print(f'sending {len(packet.encode())} bytes')
    client.send(packet.encode())

    client.close()