import pickle
import sys 
import socket

HOST = "localhost" #Using localhost using the development of the client/server files, later it will be the heroku server ip
PORT = 9876     # defaults to PORT = 9876

#Ill be using SOCKET_STREAM to connect because TCP is a requirement for the project.
#socket.SOCK_DGRAM is used for UDP connections.


#The host will receive a tuple of (host, port) instead of just each value
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


