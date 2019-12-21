import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1059))

command = "ls .. -a"

s.send(struct.pack("!H", len(command)))
s.send(bytes(command, "ascii"))

leng = s.recv(2)
leng = struct.unpack("!H", leng)[0]

cmd = ""
for i in range(leng):
    txt = s.recv(1)
    txt = txt.decode("ascii")
    cmd += txt
print(cmd)