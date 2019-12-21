import socket
import struct
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname("localhost"), 1040))

guess = 0

while guess == 0:
    n = random.randint(0, 10)
    print(f"The client's number {n}")

    s.send(struct.pack("!H", n))

    nr = s.recv(2)
    guess = struct.unpack("!H", nr)[0]
    print(f"Guess: {guess}")

    nr = s.recv(2)
    nr = struct.unpack("!H", nr)
    fullMsg = ""
    for i in range(nr):
        msg = s.recv(1)
        msg = msg.decode("ascii")
        fullMsg += msg
    time.sleep(3)
    
    print(fullMsg)
