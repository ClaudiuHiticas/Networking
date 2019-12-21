#P1_Client
import socket
import struct

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1034))

noElem = 5
lista = [1, 2, 3, 4, 5]

s.sendall(struct.pack("!H",len(lista)))
for i in lista:
    s.send(struct.pack("!H",i))

c = s.recv(5)
c = struct.unpack("!H",c)[0]
print(c)