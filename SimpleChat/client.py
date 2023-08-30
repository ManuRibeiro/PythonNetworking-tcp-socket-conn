import socket

HOST = '192.168.0.13'
PORT = 9999

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((HOST,PORT))

socket.send("Hello world".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))