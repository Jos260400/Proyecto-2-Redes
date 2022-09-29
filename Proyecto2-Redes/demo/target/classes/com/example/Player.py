from termcolor import colored
from Cards import *
from extras import *
import random

class Player():
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.deck = create_all_cards()
        
        
    def cardsPrint(self):
        for cards in self.cards:
            #print(colored(cards.number, self.color))
            print(colored(cards.get_text(), cards.color))
            
    
    def promptCard(self, previousCard):
        if previousCard != None:
            print("Previous card: " + colored(previousCard.get_text(), previousCard.color))    
        
        card = input("Type the card you want to use: (format: number/name - color:  If there's not an usable card, please type draw to get a new card: ")
        while not self.checkPlayerDeck(card, previousCard):
            clear()
            
            
            self.cardsPrint()
            print("Previous card: " + colored(previousCard.get_text(), previousCard.color))
            if card == "draw":
                self.drawCard()
            else:
                print("Card not found or not valid: ")
            #print("Card not found or not valid...")
            card = input("Type the card you want to use: (format: number/name - color:  If there's not an usable card, please type draw to get a new card: ")
            #if card == "draw":
                
        #self.cards.remove(card)
        return self.removeCards(card)
        
    def checkPlayerDeck(self, card:str, previousCard):
        for c in self.cards:
            if previousCard != None: #need to handle the special cards. 
                if str(c) == card and (previousCard.color == c.color or previousCard.number == c.number):
                    return True
            else:
                if str(c) == card:
                    return True
        return False
    
    def removeCards(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                return c
            
    
    
    def drawCard(self):
        self.cards.append(self.deck[random.randint(0, len(self.deck) - 1)])