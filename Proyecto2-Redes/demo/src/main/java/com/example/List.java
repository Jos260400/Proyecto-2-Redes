package com.example;
import com.example.Server;

public class List implements Runnable{
    
    public static void main(String[] args)  {
        Server.nameList.add("helloworld");
        
    }

    @Override
    public void run() {
        // TODO Auto-generated method stub
        for (int i = 0; i < Server.nameList.size(); i++){
            System.out.println(Server.nameList.get(i));
        }
    }

}

