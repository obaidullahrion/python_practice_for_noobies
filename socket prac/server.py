import socket
import threading
import time 

HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ADDR = (SERVER , PORT)
format = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECTED!"

server.bind(ADDR)


def handle_cline(conn , addr):
    print(f"[NEW CONNECTION] {addr} connected ")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(format)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"[LISTNING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_cline , args= (conn , addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1 }")




print("[STARTING ] server is starting....")
start()