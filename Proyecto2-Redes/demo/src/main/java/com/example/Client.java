package com.example;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;

import java.net.Socket;
import java.net.UnknownHostException;


public class Client{
	public static void main(String[] args) throws UnknownHostException, IOException, ClassNotFoundException, InterruptedException{
		InetAddress host = InetAddress.getLocalHost();
		Socket socket = null;

		ObjectInputStream ios = null;
		ObjectOutputStream oos = null;

		for (int i = 0; i <5; i++){
			socket = new Socket(host.getHostName(), 9876);
			oos = new ObjectOutputStream(socket.getOutputStream());

			System.out.println("Sending request to the server");

			if (i == 4) oos.writeObject("\nexit");

			else oos.writeObject("" + i);

			ios = new ObjectInputStream(socket.getInputStream());

			String msg = (String) ios.readObject();
			System.out.println("Message: " + msg);

			ios.close();
			oos.close();

			Thread.sleep(100);
			

		}
	}
	
}
