import socket
import sys
import threading

def threadedFunction(function):
    if function == 'isReady':
        processThread = threading.Thread(target=isReady)
        processThread.start()

def connect():
    global sock
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('Client: connecting to %s port %s' % server_address)
    sock.connect(server_address)
    host, port = sock.getpeername()
    print('Client: connected to %s on port: %s' % (host, port))

def isReady():
    print('Packet sent')
    #Sending server that client is ready
    sock.sendall(b'True')
    # Waiting for server to notify client that everyone is ready
    sock.recv(1024)
    print("All players are ready!")