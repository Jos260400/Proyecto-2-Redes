from Player import Player
from extras import clear

class Game:
    def __init__(self, player1:Player, player2:Player, player3:Player, player4:Player):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.previousCard = None
        
        self.turn = "clockwise"
        
        self.previousPlayer = 4
        
        #self.players = {'1':player1, 'email':clean_email}
        
        #self.deck = create_all_cards()
        
        
    def play(self):
        while not self.winning():
            next_player = self.getNextPlayer()
            
            if next_player == 1:
                self.player1Play()
                
            elif next_player == 2:
                self.player2Play()
                
            elif next_player == 3:
                self.player3Play()
                
            elif next_player == 4:
                self.player4Play()
                
            
            #self.player2.printCard()
            
            
            #print("--------------------------------")
            #self.player2.cardsPrint()
            #self.player2.promptCard()
            
   
    def winning(self):
        if len(self.player1.cards) == 0:
            print("Player 1 wins!")
            return True
            
        elif len(self.player2.cards) == 0:
            print("Player 2 wins!")
            return True
            
        elif len(self.player3.cards) == 0:
            print("Player 3 wins!")
            return True
            
        elif len(self.player4.cards) == 0:
            print("Player 4 wins!")
            return True
        
        else: 
            return False
            
    def reverse(self):
        if self.turn == "clockwise":
            print("Changing turn to counterclockwise")
            self.turn = "counterclockwise"
        
        elif self.turn == "counterclockwise":
            print("Changing turn to clockwise")
            self.turn = "clockwise"    
            
    
    def skip(self):
        print("Skipping...")
        
        if self.previousPlayer == 1:
            self.previousPlayer = 3
            
        elif self.previousPlayer == 2:
            self.previousPlayer = 4
            
        elif self.previousPlayer == 3:
            self.previousPlayer = 1
            
        elif self.previousPlayer == 4:
            self.previousPlayer = 2
            
            
    
    def getNextPlayer(self):
        if self.turn == "clockwise":
            if self.previousPlayer == 4:
                return 1
            else:
                return self.previousPlayer + 1
        else:
            if self.previousPlayer == 1:
                return 4
            else:
                return self.previousPlayer - 1        
        #  if self.turn == "clockwise":
        #      if self.previousPlayer == 4:
        #          return 1
             
        #      elif self.previousPlayer == 1:
        #          return 2
             
        #      elif self.previousPlayer == 2:
        #          return 3
             
        #      elif self.previousPlayer == 3:
        #          return 4
         
         
        #  elif self.turn == "counterclockwise":
        #      if self.previousPlayer == 1:
        #          return 4
             
        #      elif self.previousPlayer == 4:
        #          return 3
             
        #      elif self.previousPlayer == 3:
        #          return 2
             
        #      elif self.previousPlayer == 2:
        #          return 1
             #else:
             #    return self.previousPlayer - 1

    def plus2Card(self):
        if self.previousPlayer == 1:
            print("Player 3 will receive +2 cards")
            self.player3.plus2Card()
            #self.player2.self.cardsPrint()
            
        elif self.previousPlayer == 2:
            print("Player 4 will receive +2 cards")
            self.player4.plus2Card()
            #self.player3.self.cardsPrint()
            
        elif self.previousPlayer == 3:
            print("Player 1 will receive +2 cards")
            self.player1.plus2Card()
            #self.player4.self.cardsPrint()
            
        elif self.previousPlayer == 4:
            print("Player 2 will receive +2 cards")
            self.player2.plus2Card()
            #self.player1.self.cardsPrint()
            
    def plus4Card(self):
        if self.previousPlayer == 1:
            print("Player 3 will receive +2 cards")
            self.player3.plus4Card()
            #self.player3.self.cardsPrint()
            
        elif self.previousPlayer == 2:
            print("Player 4 will receive +2 cards")
            self.player4.plus4Card()
            
            
        elif self.previousPlayer == 3:
            print("Player 1 will receive +2 cards")
            self.player1.plus4Card()
            
        elif self.previousPlayer == 4:
            print("Player 2 will receive +2 cards")
            self.player2.plus4Card()
            
    def printPlayersDeck(self):
        if self.previousPlayer == 1:
            print("Player 2 deck is: ")
            self.player2.cardsPrint()
            #self.player3.self.cardsPrint()
            
        elif self.previousPlayer == 2:
            print("Player 3 deck is: ")
            self.player3.cardsPrint()
            
            
        elif self.previousPlayer == 3:
            print("Player 4 deck is: ")
            self.player4.cardsPrint()
            
        elif self.previousPlayer == 4:
            print("Player 1 deck is: ")
            self.player1.cardsPrint()
        
                
    def player1Play(self):
        print ("Player 1, please make  your choice...")
        self.player1.cardsPrint()
        self.previousCard = self.player1.promptCard(self.previousCard, self)
        #self.player1.cardsPrint()
        
        clear()
        if self.previousPlayer == 4:
            self.previousPlayer = 1
    
    def player2Play(self):
        print("Player 2, make your choice...")
        self.player2.cardsPrint()
        self.previousCard = self.player2.promptCard(self.previousCard, self)
        #self.player2.cardsPrint()
        
        clear()
        if self.previousPlayer == 1:
            self.previousPlayer = 2
    
    def player3Play(self):
        print("Player 3, please make your choice...")
        self.player3.cardsPrint()
        self.previousCard = self.player3.promptCard(self.previousCard, self)
        #self.player3.cardsPrint()
        
        clear()
        if self.previousPlayer == 2:
            self.previousPlayer = 3
    
    def player4Play(self):            
        print("Player 4, please make your choice...")
        self.player4.cardsPrint()
        self.previousCard = self.player4.promptCard(self.previousCard, self )
        #self.player4.cardsPrint()
        
        clear()
        if self.previousPlayer == 3:
            self.previousPlayer = 4
        
        
        