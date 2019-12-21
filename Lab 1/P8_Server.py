import socket
import sys
import os
import struct
import pickle

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('192.168.1.6', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(5)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)
        # Receive the data in small chunks and retransmit it
        pid = os.fork()
        if(pid == 0):
            leng = connection.recv(2)
            leng = struct.unpack("!H",leng)
            leng = leng[0]
            a = []
            for i in range(leng):
                nr = connection.recv(2)
                nr = struct.unpack("!H",nr)
                nr = nr[0]
                a.append(nr)
            leng = connection.recv(2)
            leng = struct.unpack("!H",leng)
            leng = leng[0]
            b = []
            for i in range(leng):
                nr = connection.recv(2)
                nr = struct.unpack("!H",nr)
                nr = nr[0]
                b.append(nr)
            common = list(set(a).intersection(b))
            print(common)
            connection.sendall(struct.pack("!H",len(common)))
            for elem in common:
                connection.sendall(struct.pack("!H",elem))
            exit()
    finally:
        # Clean up the connection
        connection.close()

