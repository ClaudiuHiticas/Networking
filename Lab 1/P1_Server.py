#P1_Server

import socket
import struct
import os
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1034))
s.listen()

while True:
    print("Waitig for connection")
    connection, client_address = s.accept()
    try:
        data = connection.recv(2)
        leng = struct.unpack("!H", data)[0]
        print("Number of elements: " + str(leng))

        suma = 0
        for i in range(leng):
            data = connection.recv(2)
            nr = struct.unpack("!H", data)[0]
            # print(nr)
            suma += nr
            print(suma)
        connection.send(struct.pack("!H", suma))
        
    finally:
        connection.close()


