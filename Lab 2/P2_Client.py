import socket
import struct, os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1066))

path = "/Users/claudiuhiticas/Desktop/University/Networking/Practice/text.txt"

s.send(struct.pack("!H", len(path)))
s.send(bytes(path, "ascii"))

nr = s.recv(2)
nr = struct.unpack("!h", nr)[0]

cmd = ""
if nr == -1:
    cmd = "echo '-1' > " + path + "-copy"
    os.system(cmd)   
else:
    fullMsg = ""
    for i in range(nr):
        msg = s.recv(1)
        msg = msg.decode("windows-1252")
        fullMsg += msg
    cmd = "echo '" + str(nr) + "\n" + fullMsg + "' > " + path + '-copy'
    os.system(cmd)
    print("Printed successfully!")