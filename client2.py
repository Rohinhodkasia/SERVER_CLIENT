import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (IP,PORT)
FORMAT = "utf-8"
SIZE = 1024
DISCONNECT_MSG = "DISCONNECT"

def main():
    client2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client2.connect(ADDR)

    connected = True
    while connected:
        #msg = client1.recv(SIZE).decode(FORMAT)
        mess  =  input("> ")
        #mess = f"Hello Server this is {ADDR}
        client2.send(mess.encode(FORMAT))
        if mess == DISCONNECT_MSG:
            connected = False
        else:
            print(client2.recv(SIZE).decode(FORMAT))
    #client2.close()
if __name__ == "__main__":
    main()