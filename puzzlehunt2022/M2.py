# Tex’s Revenge
from itertools import permutations


def isStraightOrFlush(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    
    #check flush
    if len(set(suits)) == 1:
        return True 
    #check straight
    values.sort()
    # list of straights that wrap around K-A
    wrapAroundStraights = [
        set([1, 2, 3, 13]),
        set([1, 2, 12, 13]),
        set([1, 11, 12, 13])
    ]
    
    if set(values) in wrapAroundStraights:
        return True 
    
    # check if values are not sequential
    for i in range(1, 4):
        if values[i] != values[i - 1]:
            return False 
    
    return True 
    
def main():
    # Ace to King
    values = range(1, 14)
    # 4 suits 
    suits = range(4)
    # list comprehension gets every combination of value and suit pairs to make up 52 card deck
    cards = [(value, suit) for value in values for suit in suits]
    
    # every permutation of 4 card hands
    hands = permutations(cards, 4)
    
    #numerator
    straightOrFlushHands = 0
    #denominator
    allHands = 0
    
    for hand in hands:
        allHands += 1
        if isStraightOrFlush(hand):
            straightOrFlushHands += 1
            
    print(round(straightOrFlushHands / allHands, 3))
if __name__ == "__main__":
    main()