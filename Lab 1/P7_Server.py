import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(""), 1032))
s.listen()

while True:
    print("Waiting for connection")
    connection, address = s.accept()
    try:
        idx = connection.recv(2)
        idx = struct.unpack("!H", idx)[0]
        print("idx: " + str(idx))
        lung = connection.recv(2)
        lung = struct.unpack("!H", lung)[0]
        print("lung: " + str(lung))
        lenMsg = connection.recv(2)
        lenMsg = struct.unpack("!H", lenMsg)[0]
        print("lenMsg: " + str(lenMsg))
        msg = connection.recv(lenMsg)
        msg = msg.decode("ascii")
        print(msg)

        newMsg = []
        for i in range(idx, idx + lung):
            newMsg.append(msg[i])
        print(newMsg)

        connection.send(struct.pack("!H", len(newMsg)))
        for i in newMsg:
            connection.send(bytes(i, "ascii"))

    finally:
        connection.close()
        print("Connection close")
        
        