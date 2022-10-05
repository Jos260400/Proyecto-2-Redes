from Cards import Cards
from subprocess import call 
import os


def create_all_cards():
    deck = []
    for color in ["red", "green", "blue", "yellow"]:
        for number in range(1, 10):
            deck.append(Cards(color, number, None))
        for special_ability in ["reverse", "skip", "+2", "+4"]: # , "reverse", "+2", "wild", "wild+4"
            deck.append(Cards(color, special_ability=special_ability))

    #deck.append(Cards(special_ability="+4"))
    #deck.append(Cards(special_ability="+4"))
    #deck.append(Cards(special_ability="+everything"))
    #deck.append(Cards(special_ability="+everything"))
     
    return deck

def clear():
    _ = call("clear" if os.name == "posix" else "cls") 