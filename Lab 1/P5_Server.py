import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1053))
s.listen()
 
while True:
    connection, address = s.accept()
    try:
        print(f"Connection on {address} established!")
        n = connection.recv(2)
        n = struct.unpack("!H", n)[0]

        cnt = 0
        a = []
        for i in range(1,n):
            if n % i == 0:
                cnt += 1
                a.append(i)
        
        connection.send(struct.pack("!H", cnt))
        for i in a:
            connection.send(struct.pack("!H", i))



    finally:
        connection.close()