import subprocess
import socket
from threading import Thread
import sys

def startFun(con):
    ml = multiConnection(con)
    ml.start()
class multiThread(Thread):
    def __init__(self, con, p):
        Thread.__init__(self)
        self.con = con
        self.p = p
    def run(self):
        while not self.p.stdout.closed:
            try:
                self.con.sendall(self.p.stdout.readline())
            except:
                pass
class multiConnection(Thread):
    def __init__(self, con):
        Thread.__init__(self)
        self.con = con

    def run(self):
        print("connected with backport {}".format(addr[1]))
        p = subprocess.Popen(["bc", "-i"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
        print("pid is {}".format(p.pid))
        t = multiThread(self.con, p)
        t.start()
        while True:
            try:
                data = self.con.recv(1024)
                data = data.strip()
                data = data.decode()
            except:
                pass
            try:
                if data == 'quit' or data == 'exit':
                    print("{} disconnected from server".format(addr[0]))
                    p.communicate(data.encode(), timeout=1)
                    if p.poll() is not None:
                        break
                else:
                    query = data + "\n"
                    p.stdin.write(query.encode())
                    p.stdin.flush()
            except:
                pass
        self.con.close()


host = ''
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen()
print("listing on {}".format(port))
while True:
    try:
        con, addr = s.accept()
        startFun(con)
    except:
        pass
s.close()


