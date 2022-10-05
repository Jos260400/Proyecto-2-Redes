# TODO: set first card in the pile
# Check for illegal move on the client side itself.

from pygame import error
from Cards import Card, cards
import random

class Game:
    def __init__(self, id):
        # Which player's turn is it? Initially player 1
        self.turn = 0
        
        # Are both players connected?
        self.ready = False
        
        # game Id
        self.id = id
        
        # deck
        self.deck = cards
        random.shuffle(self.deck)
        
        # player 1 cards
        self.p1Cards = self.deck[0:7]
        
        # player 2 cards
        self.p2Cards = self.deck[7:14]
        
        # player 3 cards
        self.p3Cards = self.deck[14:21]
        
        # player 4 cards
        self.p4Cards = self.deck[21:28]
        
        # In UNO only the last move matters
        self.lastMove = self.deck[28]
        
        # 7 distributed to each player + 1 on top of pile
        
        self.numCardsAssigned = 29
        
        #Two players
        self.wins = [0,0,0,0]
        
    def getLastMove(self):
        return self.lastMove 
    
    def endTurn(self):
        #self.turn = (self.turn + 1) % 2
        if self.turn == 3:
            return 0
        
        else:
            return self.turn + 1
        
        
        
        # turn = 0, resultado = 1
        # turn = 1, resultado = 0
        # turn = 2, resultado = 1
        # turn = 3, resultado = 0
        
            
            
        
    def play(self, player, move: Card):
        
        """
        @Param: player- which player's move is this?
        
        No error checking in this function. Implement before.
        """
        if move.ability != None:
            """
            In case the move has an ability, the turn is retained. No need to switch turns.
            """
            
            if move.ability == "d2":
                if player == 0:
                    self.p2Cards.append(self.deck[self.numCardsAssigned])
                    self.p2Cards.append(self.deck[self.numCardsAssigned + 1])
                    
                    
                elif player == 1:
                    self.p3Cards.append(self.deck[self.numCardsAssigned])
                    self.p3Cards.append(self.deck[self.numCardsAssigned + 1])
                    
                elif player == 2:
                    self.p4Cards.append(self.deck[self.numCardsAssigned])
                    self.p4Cards.append(self.deck[self.numCardsAssigned + 1])

                elif player == 3:
                    self.p1Cards.append(self.deck[self.numCardsAssigned])
                    self.p1Cards.append(self.deck[self.numCardsAssigned + 1])
                    
                    
                self.numCardsAssigned += 2
        	#Other abilities simply retain the turn. No need for special checkin
         
        else:
            if self.turn == 3:
                return 0
            
            else:
                return self.turn + 1
                
            #self.turn = (player + 1) 
            
        try:
            if player == 0:
                index = self.findCard(move, player)
                if index != None: del self.p1Cards[index]
                
            elif player == 1:
                index = self.findCard(move, player)
                if index != None: del self.p2Cards[index]
                
            elif player == 2:
                index = self.findCard(move, player)
                if index != None: del self.p3Cards[index]

            elif player == 3:
                index = self.findCard(move, player)
                if index != None: del self.p4Cards[index]

        except error as e:
            print("ran into error while playing move")
            
        self.lastMove = move
        
    def connected(self):
        return self.ready
    
    def findCard(self, card: Card, player):
        listOfCards = ""
        
        if player == 0:
            listOfCards = self.p1Cards
        
        elif player == 1:
            listOfCards = self.p2Cards
            
        elif player == 2:
            listOfCards = self.p3Cards
            
        elif player == 3:
            listOfCards = self.p4Cards
            
        for index in range(0, len(listOfCards)):
            if listOfCards[index] == card:
                return index
            
            return None
        
    def draw(self, player):
        """
        @Param: player- which player's move is thi
        No error checking in this function. Implement before.
        """
        
        if player == 0:
            self.p1Cards.append(self.deck[self.numCardsAssigned])
        
        elif player == 1:
            self.p2Cards.append(self.deck[self.numCardsAssigned])
            
        elif player == 2:
            self.p3Cards.append(self.deck[self.numCardsAssigned])
            
        elif player == 3:
            self.p4Cards.append(self.deck[self.numCardsAssigned])
            
        self.numCardsAssigned += 1