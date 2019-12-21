import socket,struct,threading,pickle
l_addr=[]
def work():
    while True:
        d,a=s.recvfrom(1024)
        try:
            d=pickle.loads(d)
            l_addr.append(d)
            print(f"A new user has entered the room {d[1]}")
        except:
            d=d.decode()
            print(f"User {a[1]}:{d}")


        

host='127.0.0.1'
port=1234
addr=(host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

done=False
s.sendto("salut".encode(),addr)
d,ad=s.recvfrom(1024)
d=d.decode()
print("Logged in as user:"+d)
t=threading.Thread(target=work)
t.start()

while True:
    msg=input()
    msg=msg.encode()
    for e in l_addr:
        s.sendto(msg,e)
