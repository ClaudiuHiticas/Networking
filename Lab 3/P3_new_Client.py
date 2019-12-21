import socket
import struct
import pickle
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 1033
addr = (host, port)

l_addr = []

def work():
    while True:
        d,a=s.recvfrom(1024)
        try:
            d=pickle.loads(d)
            l_addr.append(d)
            print(f"A new user has entered the room {d[1]}")
        except:
            d=d.decode()
            print(f"User {a[1]}:{d}")


done = False
s.sendto("mesaj".encode(), "ascii")
d, ad = s.recvfrom(1024)
d = d.decode()
print("Logged as Client: ", d)
t = threading.Thread(target=work)
t.start()

while True:
    msg=input()
    msg=msg.encode()
    for e in l_addr:
        s.sendto(msg,e)