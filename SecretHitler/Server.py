import socket
import sys
import threading

connections = []
addresses = []
isReady = []


def createTCP(): 
    global sock
    try:
        # Create a TCP/IP socket
        IP = 'localhost'
        PORT = 10000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = (IP,PORT)
        print('Server: starting up on %s port %s' % server_address)
        sock.bind(server_address)
        sock.listen()
    except socket.error as msg:
        print(msg)

def threadedReceive(conn): 
    while True: 
  
        # data received from client 
        data = conn.recv(1024) 
        print('Data: %s' % data)
        index = connections.index(conn)
        print(index)
        isReady[index]=True
        print(isReady)
            
        # lock released on exit 
        #threading.Lock().release() 
        break

def waitIsReady():
    global isReady
    print("Waiting for everyone to get ready")
    while False in isReady or not isReady:
        pass
    print("Everyone is ready")
    for c in connections:
        c.sendall(b'Start')

def TCPListen():
    global connections
    global addresses
    global isReady

    for c in connections:
        c.close()

    del connections[:]
    del addresses[:]
    del isReady[:]
    isReady = [False for i in isReady]

    while True:
        try:
            print(addresses)
            print('Server: waiting for a connection')
                
            # Wait for a connection
            connection, client_address = sock.accept()

            sock.setblocking(1) # prevent timeout

            #Storing connections in list
            connections.append(connection)
            #Storing adresses in list
            addresses.append(" %s %s " % (client_address))
            #Initially setting clients to not ready
            isReady.append(False)


            #threading.Lock().acquire() 
            print('Server: Client connected! %s' % client_address[0])
            processThread = threading.Thread(target=threadedReceive, args=(connection,))
            processThread.start()

                
        except socket.error as msg:
            print("Error accepting connections: %s" % msg)


    #Closing previous connections when server.py is restarted.
    
createTCP()
print("Threading TCPListen")
listenThread = threading.Thread(target=TCPListen)
listenThread.start()
print("Threading waitIsReady")
isReadyThread = threading.Thread(target=waitIsReady)
isReadyThread.start()