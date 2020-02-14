import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname(""), 1032))

msg = "This is the magic message!"
idx = 8
lung = 9

s.send(struct.pack("!H", idx))

s.send(struct.pack("!H", lung))

s.send(struct.pack("!H", len(msg)))
s.send(bytes(msg, "ascii"))

leng = s.recv(2)
leng = struct.unpack("!H", leng)[0]

newMsg = []
for i in range(0, leng):
    data = s.recv(1)
    data = data.decode("ascii")
    newMsg.append(data)

for i in newMsg:
    print(i, end = "")
print()