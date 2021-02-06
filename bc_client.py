from threading import Thread
import socket
import sys
class multithreadclient(Thread):
    def __init__(self,):
        Thread.__init__(self)
    def run(self):
        while True:
            msg = sys.stdin.readline()
            s.sendall(str(msg).encode())
            sys.stdin.flush()
            d = datarecive()
            d.start()


class datarecive(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        data =s.recv(1024)
        data = data.decode()
        print(data)

if len(sys.argv) > 1:
        host = sys.argv[1]
        port = int(sys.argv[2])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
        except:
            print("connection failed")
            pass
        print("Connected to {}. You can start sending messages...".format(host))
        t = multithreadclient()
        t.start()
else:
    exit()
