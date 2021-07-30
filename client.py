import socket

PORT = 9090

sock = socket.socket()
sock.connect(('localhost', PORT))
messages = "da"
sock.send(messages.encode("utf-8"))