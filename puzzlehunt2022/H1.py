# Brisbane is Underwater!
import math

def blocksToRemove(buildings, tallest):
    toRemove = 0
    # move left
    for i in range(tallest + 1, len(buildings)):
        if buildings[i] > buildings[i - 1]:
            toRemove += buildings[i] - buildings[i - 1]
            buildings[i] = buildings[i - 1]
    # move right
    for i in reversed(range(tallest)):
        if buildings[i] > buildings[i + 1]:
            toRemove += buildings[i] - buildings[i + 1]
            buildings[i] = buildings[i + 1]
    
    return toRemove 


def main():
    with open('brisbane.txt', 'r') as f:
        lines = f.readlines()
    
    # read in numbers to list
    buildings = []
    for line in lines:
        l = line.strip() # removes trailing \n character
        building = int(l)
        buildings.append(building)
    
    
    minToRemove = math.inf
    #  loop through each building as a tallest point
    # moving away from the tallest point, buildings need to get progressively shorter / stay the same level as the previous building
    for tallestIndex in range(len(buildings)):
        buildingsCopy = [building for building in buildings]
        toRemove = blocksToRemove(buildingsCopy, tallestIndex)
        minToRemove = min(toRemove, minToRemove)
    print(minToRemove)
if __name__ == "__main__":
    main()
    
    