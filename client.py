import socket
import sys

def client_Server():
    if len(sys.argv) < 3:
        print("Usage: python3 {} hostname port".format(sys.argv[0]))

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        s.connect((host, port))
    except:
        print("Cannot reach the {}:{}...".format(host, port))
        sys.exit(-1)

    print("connteced")

if __name__ == "__main__":
	sys.exit(client_Server())