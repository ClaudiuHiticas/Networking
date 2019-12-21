import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1053))

n = 12

s.send(struct.pack("!H", n))

cnt = s.recv(2)
cnt = struct.unpack("!H", cnt)

for i in range(cnt[0]):
    x = s.recv(2)
    x = struct.unpack("!H", x)[0]
    print(x)