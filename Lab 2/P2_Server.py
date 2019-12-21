import socket
import struct
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1066))
s.listen()

while True:
    connection, address = s.accept()
    try:
        nr = connection.recv(2)
        nr = struct.unpack("!H", nr)[0]
        
        path = ""
        for i in range(nr):
            msg = connection.recv(1)
            msg = msg.decode("ascii")
            path += msg
        
        #print(path)

        command = "cat " + path + "| wc -c"
        cmdContent = "cat " + path
        #os.system(command)
        leng = os.popen(command).read()
        cmdContentOut = os.popen(cmdContent).read()
        print(leng)
        print(cmdContentOut)
        leng = int(leng)
        if leng == 0:
            nr = -1
            connection.send(struct.pack("!h", nr))
        else:
            connection.send(struct.pack("!H", leng))
            connection.send(bytes(cmdContentOut, "windows-1252"))



    finally:
        connection.close()