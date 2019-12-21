import socket
import struct
import random
import threading

c_list = []
host = socket.gethostbyname("localhost")
port = 1036
s_addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind(s_addr)
except socket.error as msg:
    print("Error at bind: ", msg.strerror)
    exit(-1)

done = False
start=1
stop=100
random.seed()
nr=random.randint(start,stop)
winner=0

print("Server number:",nr)

while not done:
    data, addr = s.recvfrom(1024)
    if addr not in c_list:
        data = struct.unpack("!I", data)[0]
        c_list.append(addr)
        print(c_list)
        msg = "Hello client" + str(addr)
        s.sendto(bytes(msg, "ascii"), addr)
    else:
        data=struct.unpack("!I",data)[0]
        print("Client ",addr," has guessed number ",data)
        if data>nr:
            for e in c_list:
                s.sendto(bytes("S","ascii"),e)
        elif data<nr:
            for e in c_list:
                s.sendto(bytes("H","ascii"),e)
        elif data==nr:
            done=True
            winner=addr
            s.sendto(bytes("W","ascii"),winner)
            c_list.remove(winner)
            for e in c_list:
                s.sendto(bytes("L","ascii"),e)

