# UMCPC's Spies
from itertools import permutations

def numSharedUnique(name, country):
    # gets list of unique letters in a name
    uniqueName = set(list(name))
    # gets list of unique letters shared between name and country
    sharedUniques = [letter for letter in uniqueName if letter in country]
    return len(sharedUniques)

def productive(name, country):
    diffLen = abs(len(name) - len(country))
    multiplier = numSharedUnique(name, country)
    return diffLen * multiplier

def highestProductivity(productivities):
    highestScore = 0
    highestPerm = None
    perms = permutations(range(10))
    # brute force search each permutation
    for perm in perms:
        score = 0
        for i in range(10):
            score += productivities[i][perm[i]]
        
        if score > highestScore:
            highestScore = score
            highestPerm = perm
    return highestScore, highestPerm

def main():
    nameString = "Alexandra, Benjamin, Catherine, Dominic, Eleanor, Fernando, Gabrielle, Harrison, Isabella, Jeremiah"
    countryString = "Afghanistan, Bangladesh, Guatemala, Indonesia, Liechtenstein, Luxembourg, Mauritania, Montenegro, Switzerland, Turkmenistan"
    
    # put names and countries into lists with lowercase letters
    nameString = nameString.replace(",", "")
    nameString = nameString.lower()
    names = nameString.split()
    
    countryString = countryString.replace(",", "")
    countryString = countryString.lower()
    countries = countryString.split()

    # create 2d list of productivity scores between each name/country pair
    productivities = []
    for name in names:
        productivity = []
        for country in countries:
            productivity.append(productive(name, country))
        productivities.append(productivity)
    
    # brute force check every matching
    best = highestProductivity(productivities)
    print(best[0], countries[best[1][0]])
if __name__ == "__main__":
    main()