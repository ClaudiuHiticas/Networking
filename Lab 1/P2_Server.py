import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1040))
s.listen()

while True:
    connection, address = s.accept()
    print(f"Connection to {address} established!")
    try:
        lung = connection.recv(2)
        lung = struct.unpack("!H", lung)[0]
        msg = connection.recv(lung)
        msg = msg.decode("ascii")
        nr = msg.count(" ")
        
        connection.send(struct.pack("!H", nr))
        exit()


    finally:
        connection.close()