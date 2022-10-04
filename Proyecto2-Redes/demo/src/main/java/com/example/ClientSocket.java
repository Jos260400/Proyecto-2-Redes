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
    private Socket socket;
    private BufferedReader bReader;
    private BufferedWriter bWriter;
    private String user;
    //private boolean disconnected = true;

    public ClientSocket (Socket socket, String user){
        try{
            this.socket = socket;
            this.bWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            this.bReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.user = user;
            
        }catch(IOException e){
            exiting(socket, bReader, bWriter);
        }

    }

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
        int menu = 0;
        Socket socket = new Socket();
        do{ 
            System.out.println(Server.nameList.size());
            System.out.println("Please enter your username: ");
            Scanner scanner = new Scanner (System.in);
            String username = scanner.nextLine();
            System.out.println(running);
            
            if (Server.nameList.contains(username)){
                System.out.println("Username already exists");

            }
            else{
                Server.nameList.add(username);
                System.out.println("Username added");
                Server.nameList.size();
            }

            //Socket socket2 = new Socket("localhost", 4321);
            /*  
             * Menu: 
             * Option 0: Login and getting the room information              
             */
            switch(menu){
                case 0: 
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
                    SocketAddress socketAddress = new InetSocketAddress("localhost", room);  
                    socket.connect(socketAddress);
                    ClientSocket client = new ClientSocket(socket, username);
                    
                    System.out.println("Connected to the server!");
                    
                    client.listenMessage();
                    client.sendMessage();

                    // in = new DataInputStream(System.in);
                    // out = new DataOutputStream(socket.getOutputStream());

                    // String msg = "";

                    // while(!msg.equals("OVER")){
                    //     try {
                    //         msg = in.readLine();
                    //         client.sendMessage();
                    //     } catch (IOException i) {
                    //         System.out.println(i);
                    //     }
                    // }
                    
                

                    break;                    

                case 1:
                    System.out.println("Bye!");
                    in.close();
                    out.close();
                    socket.close();
                    

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
