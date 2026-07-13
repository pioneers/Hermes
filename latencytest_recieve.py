import socket
from time import sleep

server = socket.socket()

port = 8102
server.bind(("", port))

server.listen()

while True:
    client, addr = server.accept()

    message = client.recv(1024).decode()
    print(message + " recieved")
    client.send(message.encode())

    client.close()