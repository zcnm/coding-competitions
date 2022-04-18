#template
def solve(ingredients):
    indices = list(ingredients.values())
    maxServings = len(indices[0])
    for ingredient in indices:
        if len(ingredient) < maxServings:
            maxServing = len(ingredient)
    
    print(maxServings)
    for i in range(maxServings):
        soup = []
        for ingredient in indices:
            soup.append(ingredient[i])
        soup.sort()
        printArray(soup)
    return
        
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------

def main():
    ingredients = {}
    N, K = map(int, input().split())
    for i in range(N):
        ingredient = input()
        if ingredient not in ingredients:
            ingredients[ingredient] = []
        ingredients[ingredient].append(i + 1)
    solve(ingredients)

if __name__ == "__main__":
    main()