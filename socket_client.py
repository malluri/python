import socket

host="127.0.0.1"
port=5000

def main():
    fd=socket.socket()
    fd.connect((host,port))
    data=input("->")
    while data !='q':
        fd.send(data)
        data_recv=fd.recv(1024)
        print("recieved data from client:" + str(data_recv))
        data=input("->")
    fd.close()
main()
        
        
