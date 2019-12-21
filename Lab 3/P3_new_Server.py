import socket
import struct
import pickle
import threading
import copy

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 1033
addr = (host, port)

s.bind(addr)

l_addr = []

while True:
    connection, address = s.accept()
    try:
        if address not in l_addr:
            l = copy.deepcopy(address)
            l_addr.append(address)
            print("List of clients: ", l_addr)
            user = str(address).encode()[1]
            s.sendto(user, address)
            for e in l:
                aux = pickle.dumps(e)
                s.sendto(aux, address)
            aux = pickle.dumps(address)
            for e in l:
                s.sendto(aux, address)

    finally:
        connection.close()