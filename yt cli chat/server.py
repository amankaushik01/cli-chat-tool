import socket 

from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",3333))

server.listen()
all_clients={}

def client_thread(client):
    while True:
       try:
         msg = client.recv(1024)
         for c in all_clients:
             c.send(msg)
       except:
           for c in all_clients:
               if c != client:
                 c.send(f"{name} has left the chat".encode())
           del all_clients[client]
           client.close()
           break

while True: 
    print("waiting for connection..")
    client , address = server.accept()
    print("connection established")
    name=client.recv(1024).decode()
    all_clients[client]=name
    for c in all_clients:
        if c!=client:
             c.send(f"{name} has joined the chat".encode())
    
    thread = Thread(target=client_thread,args=(client,))
    thread.start()
    