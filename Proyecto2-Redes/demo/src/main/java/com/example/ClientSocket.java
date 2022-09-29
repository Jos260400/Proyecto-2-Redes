package com.example;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;

import java.util.Scanner;


public class ClientSocket {
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

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your username: ");
        String username = scanner.nextLine();

        Socket socket = new Socket("localhost", 1234);
        ClientSocket client = new ClientSocket(socket, username);

        client.listenMessage();
        client.sendMessage();

        
    }
    
}
