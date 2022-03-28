# Killing Time
import re 

def wordleSolver(wordList, guess, feedback):
    # list comprehension: creates list of words in wordlist if they follow criteria
    possibleWords = [word for word in wordList]
    for i in range(len(feedback)):
        if feedback[i] == 0:
            possibleWords = [word for word in possibleWords if guess[i] not in word]
        elif feedback[i] == 1:
            possibleWords = [word for word in possibleWords if guess[i] != word[i]]
            possibleWords = [word for word in possibleWords if guess[i] in word]
        elif feedback[i] == 2:
            possibleWords = [word for word in possibleWords if guess[i] == word[i]]
    return possibleWords

def main():
    with open('words.txt', 'r') as f:
        lines = f.readlines()
    
    # read in words to list
    words = []
    for line in lines:
        l = line.strip() # removes trailing \n character
        words.append(l)
    

    guess = "coder"
    # 0: not in word
    # 1: right letter wrong position
    # 2: right letter right position
    feedback = [0,0,0,2,1]
     
    possibleWords = wordleSolver(words, guess, feedback)
    print(possibleWords)
    print(len(possibleWords))
    
    
    """
    # regex search for possible wordle words
    r = re.compile('(?=[a-z]*r)(?![a-z]*[cod])[a-z]{3}e[^r]')
    possibleWords = list(filter(r.match, words))
    print(possibleWords)
    print(len(possibleWords))
    """
    
if __name__ == "__main__":
    main()