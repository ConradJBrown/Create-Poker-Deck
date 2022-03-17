#A standard playing card deck program
import random
def createDeck():
    #create a list for each suit and the cards
    Hearts = []
    Clubs = []
    Spades = []
    Diamonds = []
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    #use a for loop to then add each type of card to a suit
    for i in cards:
        Hearts.append(i + "H")
        Clubs.append(i + "C")
        Spades.append(i + "S")
        Diamonds.append(i + "D")
    #now add each suit to the deck
    Deck = Hearts + Clubs + Spades + Diamonds
    return Deck

def shuffle(Deck):
    for i in range(0,len(Deck)):
        swap = random.randrange(len(Deck)-1)
        Deck[i], Deck[swap] = Deck[swap], Deck[i]
        
    return Deck
def deal(n,m,Deck):
    hands = [[] for _ in range(n)]
    x = -1
    for i in range(m):
        for j in hands:
            x += 1
            j.append(Deck[x])
            print(hands)
    return hands
def main():
    Deck = createDeck()
    print(Deck)
    Shuffle = shuffle(Deck)
    print(Shuffle)
    n=int(input("How many players:"))
    m=int(input("how many cards per player:"))
    Hands = deal(n,m,Shuffle)

main()

