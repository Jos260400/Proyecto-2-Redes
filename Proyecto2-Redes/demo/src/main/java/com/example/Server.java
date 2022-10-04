package com.example;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.example.ClientSocket;
import com.example.ClientHandler;


public class Server {
    private ServerSocket serverSocket;
    static String[] userList = new String[]{};
    static List<String> nameList = new ArrayList<>(Arrays.asList(userList));
    Boolean isInTheList = false;

    public Server(ServerSocket serverSocket){
        this.serverSocket = serverSocket;
    }

    public void startServer(){
        try{

            while(!serverSocket.isClosed()){
                
                System.out.println(nameList.size());
                Socket socket = serverSocket.accept();
                System.out.println("A new client has connected");


                /*Handles all the clients information, so we can 
                have multiple clients at the same time. This will 
                run all the client tasks
                */
                ClientHandler clientHandler = new ClientHandler(socket);

                Thread thread = new Thread(clientHandler);
                thread.start();

            }
            
        }catch(IOException e){

        }
    }

    public void closeServer(){
        try{
            if (serverSocket != null){
                serverSocket.close();
            }
        }catch(IOException e){
            e.printStackTrace();
        }
    }

    // public static Boolean checkingConnection(List<String> list, String usr){
    //     System.out.println("Validating username... ");
        
    //     if (list.contains(usr) == true){

    //         isInTheList = true;
    //     }

    //     else{
    //         isInTheList = false;
    //     }

    //     return isInTheList;
    // }

    public static void main(String[] args) throws IOException{
        
        ServerSocket serverSocket = new ServerSocket(1234);
        Server server = new Server(serverSocket);
        server.startServer();

        //System.out.println(nameList);

    }
    
}