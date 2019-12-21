import socket
import struct
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname("localhost"), 1040))
s.listen()

tries = 0
while True:
    connection, address = s.accept()
    try:
        guess = 0
        while(guess == 0):
            n = connection.recv(2)
            n = struct.unpack("!H", n)[0]
            print(f"The client's number{n}")
            
            x = random.randint(0, 10)
            print(f"The server's number{x}")

            if x == n:
                guess = 1
                msg = "You win - within " + str(tries) + " tries"
                connection.send("!H", guess)
                connection.send(struct.pack("!H", len(msg)))
                connection.send(bytes(msg, "ascii"))
            else:
                tries += 1



    finally:
        connection.close()