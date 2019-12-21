import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1044))

msg = "This is the string"

s.send(struct.pack("!H", len(msg)))
s.send(bytes(msg, "ascii"))

newMsg = s.recv(len(msg))
newMsg = newMsg.decode("ascii")

print(newMsg)