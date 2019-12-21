import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1050))
s.listen()

while True:
    connection, address = s.accept()
    try:
        print(f"Conection on {address} established")
        n = connection.recv(2)
        n = struct.unpack("!H", n)[0] #5   
        print(n)
        
        a = []
        for i in range(n):
            data = connection.recv(1)
            data = data.decode("ascii")
            a.append(data)
        a.sort()
        print(a)

        m = connection.recv(2)
        m = struct.unpack("!H", m)[0] #5
        print(m)

        b = []
        for i in range(m):
            data = connection.recv(1)
            data = data.decode("ascii")
            b.append(data)
        b.sort()
        print(b)
        
        c = []
        i = 0
        j = 0

        while(i < n and j < m):
            if(a[i] < b[j]):
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        while(i < n):
            c.append(a[i])
            i += 1

        while(j < m):
            c.append(b[j])
            j += 1
        

        for i in c:
            connection.send(bytes(i, "ascii"))

        print(c)

    finally:
        connection.close()