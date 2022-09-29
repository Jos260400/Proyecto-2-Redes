from Player import Player
from extras import clear

class Game:
    def __init__(self, player1, player2, player3, player4):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.previousCard = None
        
        #self.deck = create_all_cards()
        
        
    def play(self):
        while not (self.winning()):
            print ("Player 1, please make  your choice...")
            self.player1.cardsPrint()
            self.previousCard = self.player1.promptCard(self.previousCard)
            #self.player1.cardsPrint()
            
            clear()
            
            print("Player 2, make your choice...")
            self.player2.cardsPrint()
            self.previousCard = self.player2.promptCard(self.previousCard)
            #self.player2.cardsPrint()
            
            clear()
            
            print("Player 3, please make your choice...")
            self.player3.cardsPrint()
            self.previousCard = self.player3.promptCard(self.previousCard)
            #self.player3.cardsPrint()
            
            clear()
            
            print("Player 4, please make your choice...")
            self.player4.cardsPrint()
            self.previousCard = self.player4.promptCard(self.previousCard)
            #self.player4.cardsPrint()
            
            
            
            #self.player2.printCard()
            
            
            #print("--------------------------------")
            #self.player2.cardsPrint()
            #self.player2.promptCard()
        
    def winning(self):
        if len(self.player1.cards) == 0:
            print("Player 1 wins!")
            
        if len(self.player2.cards) == 0:
            print("Player 2 wins!")
            
        if len(self.player3.cards) == 0:
            print("Player 3 wins!")
            
        if len(self.player4.cards) == 0:
            print("Player 4 wins!")
            
            
    def getRandomCard(self):
        return self.deck[random.randint(0, len(self.deck))-1]
    