import pickle
import sys 
import socket
import threading
import time

import random
from extras import create_all_cards, clear
from Player import Player
from Cards import Cards
from Game import Game


#Ill be using SOCKET_STREAM to connect because TCP is a requirement for the project.
#socket.SOCK_DGRAM is used for UDP connections.


#The host will receive a tuple of (host, port) instead of just each value
HEADER = 1024
HOST = '192.168.0.8'
PORT = 1234
s = None

MAX_CONNECTIONS = 4

userInfo = {}
users = {}


def cardsDecksGenerator():
    cards = create_all_cards()
    random.shuffle(cards)
    #11 cards for each player
    return cards[0:11], cards[11:22], cards[22:33], cards[33:44]


def createSocket():
    try:
        global s
        s = socket.socket()
        
    except socket.error as error:
        print("Socket error: %s" % error)
        
    
def bindSocket(port):
    try:
        global HOST, PORT, s
        
        PORT = int(port)
        
        s.bind((HOST, PORT)) # bind socket needs a tuple of the host and port
        s.listen(MAX_CONNECTIONS) #LIstens to a limited amount of connections
        
        print("Binding with the port %d" % PORT)
        print("The IP address is %s" % HOST)
    
    except socket.error as e:
        print("Error binding to port %d: %s" % (PORT, e) + "\nRetrying...")
        bindSocket() #If it fails, this will try again
        
        
def acceptingConnection():
    global s
    
    while True:
        try:
            connection, address = s.accept()
            s.setblocking(1) #Prevents the socket to timeout the connection
            tClient = threading.Thread(target=threadClient, args=(connection, address))
            tClient.daemon = True
            tClient.start()
            
            print("Connected request accepted from IP: %s" % address[0] + "on port: %d" % address[1]) 
            print(userInfo)
            
        except socket.error as e:
            print("Error accepting the connections: %s" % e)
            
    s.close()


   
def threadClient(connection, address):
    name = None
    while not name:
        name = connection.recv(HEADER).decode('utf-8')
        
        if not name:
            connection.send(bytes("SERVER: Select a valid username", "UTF-8"))
            
        else:
            userInfo[address[1]] = [name, connection]
            
            break
        
    
    users.update({name:address})
    print(users)
    #print(users.value("laddr"))
    connection.send(bytes(f'Server : Welcome to the server {userInfo[address[1]][0]}!', 'utf-8'))
    broadcast(address,'Joined The Chat!')
    
    #users.append(userInfo[address[1]][0])
    

    
    #p1,p2,p3,p4 = cardsDecksGenerator()
    #player1 = Player("Player 1", p1)
    #player2 = Player("Player 2", p2)
    #player3 = Player("Player 3", p3)
    #player4 = Player("Player 4", p4)

    
    #game = Game(player1, player2, player3, player4)
    #game.play()

    while True:
        cmd = connection.recv(HEADER).decode('utf-8')
        print (cmd)
        broadcast(address, cmd)
        
        if cmd == 'EXIT':
            del userInfo[address[1]]   
            break
        
        if cmd == '':
            time.sleep(5)
            return False
        
    connection.close()
    
    
def broadcast(address, cmd):
    for x in userInfo:
        try:
            if cmd == 'exit':
                if x == address[1]:
                    userInfo[x][1].send(bytes(cmd, 'utf-8'))
                    

                else:
                    userInfo[x][1].send(bytes(f'{userInfo[address[1]][0]} left the server!', 'utf-8'))
            else:
                if x != address[1]:
                    userInfo[x][1].send(bytes(f'{userInfo[address[1]][0]} : {cmd}', 'utf-8'))

        except socket.error as msg:
            print('Error in broadcasting message: ' + str(msg))



createSocket()
bindSocket(5000)
print(users)
acceptingConnection()

    
    
    
            

                  
            
            
            
        

        
        
        
    


