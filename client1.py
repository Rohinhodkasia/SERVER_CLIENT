import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (IP,PORT)
FORMAT = "utf-8"
SIZE = 1024
DISCONNECT_MSG = "DISCONNECT"

def main():
    client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client1.connect(ADDR)

    connected = True
    while connected:
        #msg = client1.recv(SIZE).decode(FORMAT)
        mess  =  input("> ")
        #mess = f"Hello Server this is {ADDR}
        client1.send(mess.encode(FORMAT))
        if mess == DISCONNECT_MSG:
            connected = False
        else:
            print(client1.recv(SIZE).decode(FORMAT))
    #client1.close()
if __name__ == "__main__":
    main()