import socket 
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER , PORT)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

def handle_clint(conn , addr):
    
    print("[NEW CONNECTION] {addr} connected")


    connected = True
    while connected:
        msg = conn.recv()


def start():
    server.listen()
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handle_clint , args=(conn , addr))
        thread.start()
        print(F"[ACTIVE CONNECTION] {threading.active_count() -1}")

print("[starting] server is starting")
start()