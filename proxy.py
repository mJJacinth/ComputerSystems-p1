'''
    Disclaimer
    tiny httpd is a web server program for instructional purposes only
    It is not intended to be used as a production quality web server
    as it does not fully in compliance with the 
    HTTP RFC https://tools.ietf.org/html/rfc2616

'''
import socket
import sys
class HTTPServer:
    '''
        Remove the pass statement below and write your code here
    '''
    def __init__(self, localhost, port_number):
    # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = (localhost, port_number)
        print(sys.stderr, 'starting up on %s port %s' % server_address)
        sock.bind(server_address)
        # print("HTTP/1.1 %d"%200)
        # Listen for incoming connections
        sock.listen()

        while True:
        # Wait for a connection
            print(sys.stderr, 'waiting for a connection')
            connection, client_address = sock.accept()
            body = "<h1>Webserver Under Construction</h1>"

            headers = ""
            headers += "HTTP/1.1 200 OK"+'\n'
            headers += "Content-Type: text/html "+'\r\n'
            headers += "Content-Length: %s "%str(len(body))+'\r\n'
            headers += "Connection: close "+'\r\n'
            headers += "\n"
            data = bytes(headers+body,'utf-8')
            connection.sendall(data)

            connection.close()



def main():
    # test harness checks for your web server on the localhost and on port 8888
    # do not change the host and port
    # you can change the HTTPServer object if you are not following OOP
    HTTPServer('127.0.0.1', 8888)

if __name__ == "__main__":
    main()