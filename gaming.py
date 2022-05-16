import socket
import sys
import random
 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")
 
serverAddress=('localhost',10000)
 
s.bind(serverAddress)
print("server binded")
 
s.listen()
 
while True:
    print("waiting for a connection")
    connection, client_add= s.accept()
    message = connection.recv(1024).decode()
    print("got connection from", client_add)
    print(message)
    secret=random.randint(0,9)
    count=0
    connection.send("Ready".encode())
   
   
    # try:
    print("connection from", client_add)
    while True:
        rec_data = int(connection.recv(1024).decode())
        print("recieved", rec_data)
        if rec_data==secret:
            connection.sendall("correct".encode())
            connection.close()
            break
        elif rec_data<secret:
            connection.sendall("low".encode())
            count+=1
        elif rec_data>secret:
            connection.sendall("high".encode())
            count+=1

 
    # finally:
    connection.close()

