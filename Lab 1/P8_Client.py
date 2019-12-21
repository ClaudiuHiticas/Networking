__author__ = 'dadi'
#import socket for all socket related primitives
import socket
import pickle
# we need struct in order to be able to pack data in
# a stream of bytes so that we can actually send
# an integer as a binary four byte sequence - instead
# of a string
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# The obscure struct_addr is elegantly replaced by
# a simple pair - very convenient. Replace the IP Address with
# the one of your server
s.connect( ("192.168.1.6",10000) )

# pack the value of a as a short int (16 bits) in network representation
a = [1000,2,3,6,7]

res = s.sendall(struct.pack("!H",len(a)))
for x in a:
    res = s.sendall(struct.pack("!H",x))

b = [2,3,3,5]

res = s.sendall(struct.pack("!H",len(b)))
for x in b:
    res = s.sendall(struct.pack("!H",x))

# unpack the content read from the network into a short int
# and convert from network representation back to host
leng = s.recv(2)
leng = struct.unpack("!H",leng)
leng = leng[0]
common = []
for i in range(leng):
    nr = s.recv(2)
    nr = struct.unpack("!H",nr)
    nr = nr[0]
    common.append(nr)
print(common)

s.close()
 
