'''
    Disclaimer
    tiny httpd is a web server program for instructional purposes only
    It is not intended to be used as a production quality web server
    as it does not fully in compliance with the 
    HTTP RFC https://tools.ietf.org/html/rfc2616

'''
import socket
class HTTPServer:
    '''
        Remove the pass statement below and write your code here
    '''
    def __init__(self,IP,port):
        self.ip=IP
        self.portnum=port
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip,self.portnum))
        s.listen(1)
        while True:
            print("waiting for connection")
            conn, cl_add=s.accept()
            print("connection from", cl_add)
            try:
                data=conn.recv(1024)
                content = "<h1 align = \"center\">Webserver Under construction</h1>"
                response_body= "'HTTP/1.0 200 OK\n\n"+content
                response_headers='Content-Type : text/html,Content-Length:1024,Connection : close'
                response_body=response_body+response_headers
                print("sending data")
                conn.sendall(response_body.encode())
            finally:
                conn.close()

    pass

def main():
    # test harness checks for your web server on the localhost and on port 8888
    # do not change the host and port
    # you can change  the HTTPServer object if you are not following OOP
    obj=HTTPServer('127.0.0.1', 10000)

if __name__ == "__main__":
    main()
