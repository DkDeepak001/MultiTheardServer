import socket
import select as sel
import sys
host =""
port =4444
socketList =[]
def multi_Server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host , port))
    s.listen(10)
    socketList.append(s)
    print("MultiThreadedChat is Listeing On " + str(port) + "....")
    while True:
            #Waiting For someone To Connect
            ready_read,ready_write,error=sel.select(socketList,[],[],0)
            for sock in ready_read:
                if sock == s:
                    client_socket , addr = s.accept()
                    socketList.append(client_socket)
                    print("Client {}:{} connected.".format(addr[0], addr[1]))
                else:
                    print("Connection Lost!")
                    s.close()
if __name__ == "__main__":
    sys.exit(multi_Server())