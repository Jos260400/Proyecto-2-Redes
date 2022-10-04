package com.example;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;
import java.net.UnknownHostException;

import java.util.Scanner;


public class ClientSocket {
    private static DataInputStream in;
    private static DataOutputStream out;
    private static Socket socket;
    private BufferedReader bReader;
    private BufferedWriter bWriter;
    private String user;
    
    // public static void printMenu(){
    //     System.out.println
    //     (""" 
    //         1. Login
    //         2. Exit
            
    //     """);

    // }
    //private boolean disconnected = true;

    public ClientSocket (Socket socket, String user){
        try{
            ClientSocket.socket = socket;
            this.bWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            this.bReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.user = user;
            
        }catch(IOException e){
            exiting(socket, bReader, bWriter);
        }

    }

    // public void disconnectClient()
    // {
    //     try{
    //         socket.close();
    //         System.out.println("Please enter a new port to connect to.");
    //         Scanner scan = new Scanner(System.in);
    //         int roomScan = scan.nextInt();
    //         SocketAddress sAddress = new InetSocketAddress("192.168.0.8", roomScan);  
    //         socket.connect(sAddress); 


    //     }
    //     catch(IOException e){
    //         exiting(socket, bReader, bWriter);
    //     }
    // }

    public void sendMessage(){ 
        try{
            bWriter.write(user);
            bWriter.newLine();
            bWriter.flush();
            Scanner sc = new Scanner(System.in);

            while(socket.isConnected()){

                String sendMsg = sc.nextLine();
                //Exit in progress

                if(sendMsg.contains("EXIT")){
                    System.out.println("BYE");
                    //disconnected = false;
                    //disconnectClient();
                    socket.close();

                    System.out.println("Please enter a new port to connect to.");
                    Scanner scan = new Scanner(System.in);
                    int roomScan = scan.nextInt();
                    SocketAddress sAddress = new InetSocketAddress("192.168.0.8", roomScan);  
                    socket.connect(sAddress); 
                    break;
                    
                    
                }
                bWriter.write(user + ": " + sendMsg);
                bWriter.newLine();
                bWriter.flush();
            }

        }catch(IOException e){
            exiting(socket, bReader, bWriter);
        }

    }

    public void listenMessage(){
        new Thread(new Runnable() {
            @Override
            public void run(){
                String groupChatMSG;

                while(socket.isConnected()){
                    try{
                        groupChatMSG = bReader.readLine();
                        System.out.println(groupChatMSG);   
                    }
                    catch(IOException e){
                        exiting(socket, bReader, bWriter);
                    }

                    
                }
            }
        }).start();
    }
    

    public void exiting(Socket socket, BufferedReader bReader, BufferedWriter bWriter){
        try{
            if(bReader !=null){
                bReader.close();
            }

            if(bWriter != null){
                bWriter.close();
            }

            if(socket != null){
                socket.close();
            }
        }catch(IOException e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws UnknownHostException, IOException{
        //Socket socket = new Socket("localhost", 1234);
        boolean running = true;
        int menu = 1;
        socket = new Socket();


        do{ 
            
            switch(menu){
            
                case 1: 
                    System.out.println(Server.nameList.size());

                    System.out.println("Please enter your username: ");
                    Scanner scanner = new Scanner (System.in);
                    String username = scanner.nextLine();


                    System.out.println("Welcome to the UNO game socket implementation!" + username);
                    System.out.println(running);
                    /*
                     * Login
                     */
                    System.out.println("Please enter the room number");

                    String roomString = scanner.nextLine(); 
                    System.out.println("Loading room " + roomString + "...");
                    int room = Integer.parseInt(roomString);
                    
                    //TO DO: We need to get the the public ip address of the server...
                    SocketAddress socketAddress = new InetSocketAddress("192.168.0.8", room);  
                    //socket.connect(socketAddress);
                    socket.connect(socketAddress);
                    ClientSocket client = new ClientSocket(socket, username);
                    
                    System.out.println("Connected to the server!");
                    
                    client.listenMessage();
                    client.sendMessage();
                    //client.disconnectClient();

                    //From here we will implement the actual UNO game...
                                        
                

                    break;                    

                default:
                    System.out.println("Please enter a valid menu item!");
                    running = false;
                    break;
            }
        }while(running);
        // Scanner scanner = new Scanner(System.in);
        // System.out.println("Enter your username: ");
        // String username = scanner.nextLine();

        // Socket socket = new Socket("localhost", 1234);
        // ClientSocket client = new ClientSocket(socket, username);

        //client.listenMessage();
        //client.sendMessage();

        
    }
    
}
