import socket


HEADER = 64
SERVER = "192.168.0.108"
PORT = 5050
format = "utf-8"
clint = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ADDR = (SERVER , PORT)
DISCONNECT_MESSAGE = "DISCONNECTED!"

clint.connect(ADDR)
while True:
    try:
        text = input("msg: ")
        def send(msg):
            message = msg.encode(format)
            msg_length = len(message)
            send_length = str(msg_length).encode(format)
            send_length += b' ' *(HEADER - len(send_length))
            clint.send(send_length)
            clint.send(message)


        send(text)
    except KeyboardInterrupt:
        send(DISCONNECT_MESSAGE)
        break
