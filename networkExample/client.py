import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

clientSocket.connect((host,port))

msg = clientSocket.recv(2048)

clientSocket.close()

print(msg.decode('ascii'))