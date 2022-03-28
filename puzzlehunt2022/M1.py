# Le Débat Français
def getUniqueScore(substring):
    # seen dictionary tracks which letters we have already seen
    seen = {}
    uniqueLetters = 0
    for letter in substring:
        if letter not in seen:
            seen[letter] = 0
            uniqueLetters += 1
    return uniqueLetters 

def main():
    with open('french.txt', 'r') as f:
        french = f.read()
    
    letters = ""
    # remove all non alphabet characters (including spaces and \n)
    for letter in french:
        if letter.isalpha():
            letters += letter.lower()
    
    mostUniqueScore = 0
    mostUniqueSubstring = ""
    for i in range(0, len(letters) - 30):
        substring = letters[i:i + 30]
        
        uniqueScore = getUniqueScore(substring)
        if uniqueScore > mostUniqueScore:
            mostUniqueScore = uniqueScore
            mostUniqueSubstring = substring 
    
    print(mostUniqueSubstring)
if __name__ == "__main__":
    main()