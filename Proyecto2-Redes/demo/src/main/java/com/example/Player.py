from termcolor import colored
from extras import create_all_cards, clear
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
                    return True
            else:
                if str(c) == card:
                    if c.special_ability == "reverse":
                        print("reversing the flow...")
                        game.reverse()
                    if c.special_ability == "skip":
                        game.skip()
                    return True
        return False

    
    def removeCards(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                return c
            
    
    
    def drawCard(self):
        #print("Getting a new card...")
        self.cards.append(self.deck[random.randint(0, len(self.deck) - 1)])
        
