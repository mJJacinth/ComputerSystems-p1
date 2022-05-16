import mimetypes
import socket
import os
 
class HTTPServer:
# creating a constructor
    def __init__(self,address,port):
        self.addres=address
        self.portnum=port
        server_address=(self.addres,self.portnum)
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(server_address)
        sock.listen()
        while True:
            connection,Client_address=sock.accept()
            print('connection ready')
            data=connection.recv(1024).decode()
            print('******\n',data)
            dir=data.splitlines()[0].split(" ")[1][1:]
            print(dir)
            URL="http://127.0.0.1:8888/"
            dir=dir.replace('/','\\')
 
            root=os.getcwd()
            dir_path= os.path.join(root,dir)
            if os.path.isdir(dir_path):
                dir_files=os.listdir(dir_path)
                response_status= 'HTTP/1.1 200 \n'
                response_body=""
                for file in dir_files:
                    print("^^^",file,"^^^^")
                    response_body+=f'<a href={URL+ dir_path+"/"+file} align="center">{file}</a></br>'
                    response_header=f'Content-Type: text/html\nContent-Length:{len(response_body)}\nConnection:close\n\n'
                    final_response= response_status+response_header+response_body
                connection.sendall(final_response.encode())
            elif  os.path.isfile(dir_path):
                f=open(dir_path,'rb')
                file_content=f.read()
                f.close()
                response_status= 'HTTP/1.1 200 \n'
                response_header=f'Content-Type:{mimetypes.guess_type(dir_path)}\nContent-Length:{len(file_content)}\nConnection:close\n\n'
                final_response= (response_status+response_header).encode()+file_content
                connection.sendall(final_response)
            else:
                content = "<h1 align=\"center\"> Not found </h1>"
                response_status= "'HTTP/1.1 404 not found\n"
                response_headers=f'Content-Type:text/html\nContent-Length:{len(content)}\nConnection:close\n\n'
                response=response_status+response_headers+content
                print("sending data")
                connection.sendall(response.encode())
            connection.close()
            pass
   
    pass
 
def main():
    # test harness checks for your web server on the localhost and on port 8888
    # do not change the host and port
    # you can change  the HTTPServer object if you are not following OOP
    serv_obj=HTTPServer('127.0.0.1',8888)
 
 
if __name__ == "__main__":
    main()