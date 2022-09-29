import random
from extras import create_all_cards, clear
from Player import Player
from Cards import Cards
from Game import Game

def cardsDecksGenerator():
    cards = create_all_cards()
    random.shuffle(cards)
    #11 cards for each player
    return cards[0:11], cards[11:22], cards[22:33], cards[33:44]

p1,p2,p3,p4 = cardsDecksGenerator()
player1 = Player("Player 1", p1)
player2 = Player("Player 2", p2)
player3 = Player("Player 3", p3)
player4 = Player("Player 4", p4)

#clear()
game = Game(player1, player2, player3, player4)
game.play()

#player1.cardsPrint()