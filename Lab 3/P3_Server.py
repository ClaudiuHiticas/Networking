import socket,struct
import pickle,copy

host='127.0.0.1'
port=1234
s_addr=(host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(s_addr)


l_addr=[]

while True:
    data,addr=s.recvfrom(1024)
    if addr not in l_addr:
        l=copy.deepcopy(l_addr)
        l_addr.append(addr)
        print("List of users:"+str(l_addr))
        user=str(addr[1]).encode()
        s.sendto(user,addr)
        for e in l:
            aux=pickle.dumps(e)
            s.sendto(aux,addr)
        aux=pickle.dumps(addr)
        for e in l:
            s.sendto(aux,e)
