import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

serverSocket.bind((host, port))

serverSocket.listen(10)

while True:
    clientSocket, addr = serverSocket.accept()
    print("Connection From %s" %(str(addr)))

    msg = "Thanks 4 connecting..."+"\r\n"

    clientSocket.send(msg.encode('ascii'))
    clientSocket.close()