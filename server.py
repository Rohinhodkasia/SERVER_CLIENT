import socket
import threading

import wikipedia

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNECT"


def handle_client(conn, address):
    print(f"Connected with {address}")
    connected = True
    while connected:
        msg: object = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
            # conn.close()
        print(f'{address} :{msg}')
        mess = input("> ")
        #msg = wikipedia.summary(msg, sentences=1)
        conn.send(msg.encode())
    # print(f"[ACTIVE CONNECTION ] : {threading.activeCount()-1}")

    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[Connection] Server Created Successfully with IP {IP} : PORT {PORT}")
    server.bind(ADDR)
    server.listen(5)
    print(f"[LISTENING] server is listening ...")

    while True:
        conn, address = server.accept()
        # c.send("Thanks For connecting with us".encode())
        thread = threading.Thread(target=handle_client, args=(conn, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] : {threading.activeCount() - 1} ")


if __name__ == "__main__":
    main()
