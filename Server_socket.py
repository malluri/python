import socket

def main():
    host="127.0.0.1"
    port=5000
    sock_fd=socket.socket()
    sock_fd.bind((host,port))
    sock_fd.listen(1)
    c,addr=sock_fd.accept()
    print("address:" + str(addr))
    while True:
        data=c.recv(1024)
        if not data:
            break
        print("data from client:" + str(data))
        sdata=str(data).upper()
        c.send(sdata)
    sock_fd.close()

main()
