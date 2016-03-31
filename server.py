import socket
import threading
import pdb

SOCKET_DICT={}
SOCKET_LIST=[]
THREAD_LIST=[]
BUF_SIZE=1024

def send_message(c_id,message):
    SOCKET_DICT[c_id].send(message)

def broadcast(message):
    for soc in SOCKET_LIST:
        soc.send(message)

class clientThread(threading.Thread):
    def __init__(self,client_sock,id):
        threading.Thread.__init__(self)
        self.conn=client_sock
        self.id=id
        self.isRun=1
        #self.conn.send('You are connected')
    def run(self):
        while True and self.isRun:
            inp=self.conn.recv(BUF_SIZE).split(' ')
            print '---> ',inp
#            pdb.set_trace()
            if int(inp[0])==1: #send to person
                c_id=inp[1]
                message=inp[2]
                send_message(c_id,message)
            if int(inp[0])==2: #send to all
                message=inp[1]
                broadcast(message)
            if int(inp[0])==3:
                break
    def _stop(self):
        self.isRun=False

host='127.0.0.1'
port=12345

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
try:
    while True:
        conn,addr= s.accept()
        print 'got connection from ',addr
        t_id=conn.recv(BUF_SIZE)
        t_thread=clientThread(conn,t_id)
        t_thread.start()
        SOCKET_LIST.append(conn)
        SOCKET_DICT[t_id]=conn
        THREAD_LIST.append(t_thread)

except KeyboardInterrupt:
    for c in THREAD_LIST:
        c._stop()
