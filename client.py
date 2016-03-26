import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=12345
BUF_SIZE=1024

class cThread(threading.Thread):
    def __init__(self,server_sock,ID):
        threading.Thread.__init__(self)
        self.server_sock=server_sock
        self.ID=ID
        self.server_sock.send(ID)
    def run(self):
        while True:
            tout=self.server_sock.recv(BUF_SIZE)
            print tout

ID=raw_input("ID:")
s.connect((host,port))
thread=cThread(s,ID)
thread.start()
while True:
    #header='2\n'
    tinp=raw_input()
    #header+=tinp
    if tinp=='end':
        return 1
    s.send(tinp)



