import socket
from time import time, sleep
import sys
from os import get_terminal_size

port = 8102

last_three = sys.argv[1]

raspi_ip = "192.168.0." + last_three
# for testing
# raspi_ip = "127.0.0.1"

times = []
time_between_packets = 0.1 # time between packets in seconds
packet_size = 20 # packet size in bytes
packet_count = 0
connection_good = True

while True:
    sleep(time_between_packets)
    message = str(packet_size)

    client = socket.socket()

    sendtime = time()

    try: 
        client.connect((raspi_ip, port))
    except ConnectionRefusedError:
        connection_good = False
        terminal_dims = get_terminal_size()
        print("\n" * (terminal_dims[1] // 2))
        print("Connection dropped!")
        print("\n" * (terminal_dims[1] // 2 - 1 + (terminal_dims[1] % 2)))
        continue
    client.send(message.encode())

    if not connection_good:
        connection_good = True
        continue

    gettime = time()
    times.append(gettime - sendtime)
    if packet_count * time_between_packets > 60:
        times.pop(0)
    else:
        packet_count += 1

    terminal_dims = get_terminal_size()
    print("\n" * (terminal_dims[1] // 2))
    print("Avg time to travel through socket: " + str(sum(times) / packet_count * 1000) + " milliseconds")
    print("\n" * (terminal_dims[1] // 2 - 1 + (terminal_dims[1] % 2)))

    client.close()

    