import socket
import struct
import random
import time

host = socket.gethostbyname("localhost")
port = 1036
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

done = False
start = 1
stop = 100
random.seed()


nr = random.randint(start, stop)
s.sendto(struct.pack("!I", nr), addr)
d,ad=s.recvfrom(1024)
print(d.decode("ascii"))

while not done:
    nr=random.randint(start,stop)
    s.sendto(struct.pack("!I",nr),addr)
    d,ad=s.recvfrom(1024)
    d=d.decode("ascii")

    print(d)
    if d=="H":
        start=nr
    if d=="S":
        stop=nr
    if d=="W" or d=="L":
        done=True
    time.sleep(3)

if d=="L":
    print("I lost")
else:
    print("I won")
