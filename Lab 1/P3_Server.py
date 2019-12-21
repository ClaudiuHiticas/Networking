import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1044))
s.listen()

while True:
    connection, address = s.accept()
    print(f"Connection on {address} established!")

    try:
        lung = connection.recv(2)
        lung = struct.unpack("!H", lung)[0]

        msg = connection.recv(lung)
        msg = msg.decode("ascii")

        newMsg = msg[::-1]
        
        connection.send(bytes(newMsg, "ascii"))

    finally:
        connection.close()


