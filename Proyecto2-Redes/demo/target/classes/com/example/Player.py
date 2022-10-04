from termcolor import colored
from extras import create_all_cards, clear
import random

class Player():
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.deck = create_all_cards()
        self.ready = False
        
    def connected(self):
        return self.ready
        
    def cardsPrint(self):
        for cards in self.cards:
            #print(colored(cards.number, self.color))
            print(colored(cards.get_text(), cards.color))
            
            
    def playerStatus(self):
        self.status = False
        
    
    def promptCard(self, previousCard, game):
        if previousCard != None:
            print("Previous card: " + colored(previousCard.get_text(), previousCard.color))    
        
        card = input("Type the card you want to use: (format: number/name - color:  If there's not an usable card, please type draw to get a new card: ")
        while not self.checkPlayerDeck(card, previousCard, game):
            clear()
            
            print("Current player: " + self.name)
            self.cardsPrint()
            print("Previous card: " + colored(previousCard.get_text(), previousCard.color))
            
            if card == "draw":
                print("Getting a new card...")
                self.drawCard()
                
            
            else:
                print("Card not found or not valid: ")
            #print("Card not found or not valid...")
            card = input("Type the card you want to use: (format: number/name - color:  If there's not an usable card, please type draw to get a new card: ")
            #if card == "draw":
                
        #self.cards.remove(card)
        return self.removeCards(card)
        
    def checkPlayerDeck(self, card: str, previousCard, game):
        for c in self.cards:
            if previousCard != None: # need to handle special card, such as everything, stack, etc.
                if str(c) == card and (previousCard.color == c.color or previousCard.number == c.number):
                    if c.special_ability == "reverse":
                        print("reversing the flow...")
                        game.reverse()
                    if c.special_ability == "skip":
                        game.skip()
                        
                    if c.special_ability == "+2":
                        self.plus2Card()
                    
                    if c.special_ability == "+4":
                        self.plus2Card()
                    
                    return True
            else:
                if str(c) == card:
                    if c.special_ability == "reverse":
                        game.reverse()
                    
                    if c.special_ability == "skip":
                        game.skip()
                    
                    if c.special_ability == "+2":
                        game.plus2Card()
                        
                    if c.special_ability == "+4":
                        game.plus4Card()
                        
                    return True
        return False

    
    def removeCards(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                return c
            
    
    
    def drawCard(self):
        #print("Getting a new card...")
        randomCard = self.deck[random.randint(0, len(self.deck) - 1)]
        self.cards.append(randomCard)
        

    def plus2Card(self):
        for i in range(0,2):
            #print(i)   
            randomCards = self.deck[random.randint(0, len(self.deck) - 1)]
            self.cards.append(randomCards)
            print(colored(randomCards.get_text(), randomCards.color))
            #print(self.cards.append(self.deck[random.randint(0, len(self.deck) - 1)]))
            
            
    def plus4Card(self):
        for i in range(0,4):
            #print(i)
            randomCards = self.deck[random.randint(0, len(self.deck) - 1)]
            self.cards.append(randomCards)
            print(colored(randomCards.get_text(), randomCards.color))
            #self.cards.append(self.deck[random.randint(0, len(self.deck) - 1)])
            #print(self.cards.append(self.deck[random.randint(0, len(self.deck) - 1)]))
            
            