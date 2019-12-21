import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1026))
s.listen()

while True:
    connect, address = s.accept()
    try:
        print(f"Connection on {address} established!")
        n = connect.recv(2)
        n = struct.unpack("!H", n)[0]
        
        fullMsg = ""
        for i in range(n):
            msg = connect.recv(1)
            msg = msg.decode("ascii")
            fullMsg += msg
    
        print(fullMsg)
        a = connect.recv(1)
        a = a.decode("ascii")
        print(a)

        l = []
        for i in range(0, len(fullMsg)):
            if(fullMsg[i] == a):
                l.append(i)

        connect.send(struct.pack("!H", len(l)))
        for i in range(len(l)):
            connect.send(struct.pack("!H", l[i]))


    finally:
        connect.close()