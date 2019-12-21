import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1040))

msg = "This is the message which I would to send!" #8 spaces

s.send(struct.pack("!H", len(msg)))
s.send(bytes(msg, "ascii"))

nr = s.recv(2)
nr = struct.unpack("!H", nr)

print(nr[0])