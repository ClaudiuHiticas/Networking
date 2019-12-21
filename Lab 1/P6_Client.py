import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1026))

msg = "Ana has apples"
a = 'a'

s.send(struct.pack("!H", len(msg)))
s.send(bytes(msg, "ascii"))
s.send(bytes(a, "ascii"))

leng = s.recv(2)
leng = struct.unpack("!H", leng)[0]

el = 0
l = []
for i in range(leng):
    el = s.recv(2)
    el = struct.unpack("!H", el)[0]
    l.append(el)

print(l)