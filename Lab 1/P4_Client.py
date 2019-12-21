import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1050))

n = 5
a = ['q', 'w', 'e', 'r', 't']

s.send(struct.pack("!H", n))
for i in a:
    s.send(bytes(i, "ascii"))

m = 5
b = ['a', 's', 'd', 'f', 'g']

s.send(struct.pack("!H", m))
for i in b:
    s.send(bytes(i, "ascii"))

c = []
for i in range(n + m):
    data = s.recv(1)
    data = data.decode("ascii")
    c.append(data)
print(c)
