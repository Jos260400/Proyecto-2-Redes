package com.example;


import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.ClassNotFoundException;

import java.net.ServerSocket;
import java.net.Socket;

public class ServerTesting{
	private static ServerSocket serverSocket;
	private static int port = 9876;

	public static void main(String args[]) throws IOException, ClassNotFoundException{
		serverSocket = new ServerSocket(port);

		while(true){
			System.out.println("Waiting for the client request");
			Socket socket = serverSocket.accept();

			//Input to then be registered by the socket
			ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());

			String msg = (String) ois.readObject();

			System.out.println("Message Received: " + msg);

			ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());

			oos.writeObject("Hi Client" + msg);

			ois.close();

			oos.close();

			if(msg.equalsIgnoreCase("exit")) break;

		}


		System.out.println("Shutting down the server");
		serverSocket.close();

	}
}