import socket
import sys
 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
name = input("Enter your name ")
sock.send(bytes("Hi %s"% name,'utf-8'))#("Hi %s"%name).encode()
server_reply=sock.recv(1024).decode()
if server_reply=="Ready":
    count=0
    # try:
    while True:
    # Send data
        number=input("enter the number between 0 to 9 \n")
        message = number.encode()
        # message = 'This is the message. It will be repeated.'
        # print(sys.stderr, 'sending "%s"' % message)
        sock.send(message)

        # Look for the response
        result_req= "correct"
        server_data=sock.recv(1024).decode()
        # amount_expected = len(message)
        print(server_data)    
        if result_req == server_data:
            print("took", count+1, " times to guess right")
            break
        else:
            count=count+1    
 
    # finally:
    #     print('closing socket')
    sock.close()
