import socket
from time import time, sleep
import sys

port = 8102

last_three = sys.argv[1]

raspi_ip = "192.168.0." + last_three

times = []
trials = 20

for i in range(trials):
    """
    message = input()
    if message == "stop":
        break
    """
    sleep(0.1)
    message = "Hello"

    client = socket.socket()

    sendtime = time()

    client.connect((raspi_ip, port))
        
    client.send(message.encode())

    print(client.recv(1024).decode() + " recieved")
    gettime = time()
    times.append(gettime - sendtime)

    client.close()

if trials > 0:
    print("Avg time to travel through socket: " + str(sum(times) / trials * 1000))