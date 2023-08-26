import socket

#host and port were the server will be running
HOST = '192.168.0.13'
PORT = 9999
#socket for accepting connection in tcp
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
#define that server os listening
server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connnected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message! Thank you".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")