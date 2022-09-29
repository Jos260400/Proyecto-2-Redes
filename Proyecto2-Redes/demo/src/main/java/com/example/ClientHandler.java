package com.example;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.ArrayList;

public class ClientHandler implements Runnable{

    public static ArrayList<ClientHandler> handlers = new ArrayList<>();
    private Socket socket; 
    private BufferedReader bReader;
    private BufferedWriter bWriter;
    private String clientUser;

    public ClientHandler(Socket socket){
        try{
            this.socket = socket;
            this.bWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            this.bReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.clientUser = bReader.readLine();
            
            handlers.add(this);
            
            broadCastMessage("SERVER: " + clientUser + " has joined...");

        }catch(IOException e){
            exiting(socket, bReader, bWriter);
        }
    }



    @Override
    public void run() {
        // TODO Auto-generated method stub
        String msgFromClient;
        
        while (socket.isConnected()){
            try{
                msgFromClient = bReader.readLine();
                broadCastMessage(msgFromClient);

            }catch (IOException e){
                exiting(socket, bReader, bWriter);
                break;
            }
        }
    }

    public void broadCastMessage(String msgToEveryone){
        for(ClientHandler clientHandler: handlers){
            try{
                if(!clientHandler.clientUser.equals(clientUser)){
                    clientHandler.bWriter.write(msgToEveryone);

                    clientHandler.bWriter.newLine();

                    clientHandler.bWriter.flush();
                }
            }catch(IOException e){
                exiting(socket, bReader, bWriter);
            }
        }
    }

    public void removeClient(){
        handlers.remove(this);

        broadCastMessage("SERVER: " + clientUser + "is leaving...");
    }

    public void exiting(Socket socket, BufferedReader bReader, BufferedWriter bWriter){
        removeClient();
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
}
