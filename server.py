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
            read_ready, write_ready, error = sel.select(socketList, [], [])
            for sock in read_ready:
                if sock == s:
                    client_socket , addr = s.accept()
                    socketList.append(client_socket)
                    print("Client {}:{} connected.".format(addr[0], addr[1]))
                    broadcast(s,client_socket, "{} entered our chatting room... \n".format(addr))
                else:
                    try:
                        data = sock.recv(10)
                        data =data.decode()
                        if data:
                            print(data)
                        else:
                            print("client {}: offline".format(addr[1]))
                            if sock in socketList:
                                socketList.remove(sock)
                    except:
                        print("client Except")
                    continue

def broadcast(server_socket, client_socket, message):
    print("mssegae" + message)
    for socket in socketList :
        if socket != server_socket and socket != client_socket:
            try:
                socket.send(message.encode())
            except:
                socket.close()
                if socket in socketList:
                    socketList.remove(socket)

if __name__ == "__main__":
    sys.exit(multi_Server())