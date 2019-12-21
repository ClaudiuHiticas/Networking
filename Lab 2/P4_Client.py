import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1030))

n = 5
a = [2.5, 3.6, 2.1, 7.3, 3]

s.send(struct.pack("!H", n))
for i in a:
    s.send(struct.pack("!e", i))

