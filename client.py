import socket
import threading
import select

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
        self.isRunning=True
    def run(self):
        while self.isRunning:
            ready=select.select([self.server_sock],[],[])
            if ready[0]:
                tout=self.server_sock.recv(BUF_SIZE)
                print tout
    def _stop(self):
        self.isRunning=False

ID=raw_input("ID:")
s.connect((host,port))
thread=cThread(s,ID)
thread.start()
ha=True
while ha:
    tinp=raw_input()
    if tinp=='3':
        print ha
        ha=False
        thread._stop()
    s.send(tinp)
thread.join()



