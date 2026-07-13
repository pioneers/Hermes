import socket
from time import sleep

sock = socket.socket()
port = 8101

sock.bind(("",port))

sock.listen()

while True:
    c, addr = sock.accept()
    print("Got connection from " + str(addr))
    sleep(30)
    c.close()
    break