# Peaking

def getRegions(mountains, GRID_SIZE):
    regions = {}
    adjacentMountains = {}
    visited = {}
    # give each region a unique identifier
    regionCounter = 0
    
    #breadth first search to find all mountains of a region
    def bfs(current):
        # flag to not check mountain again
        visited[current] = 0
        x, y = current 
        # add mountain to region
        regions[regionCounter].append(mountains[x][y])
        
        # check left and right
        for dx in [-1 ,1]:
            if 0 <= x + dx < GRID_SIZE:
                # if mountain not part of same region, add to adjacent list
                if mountains[x + dx][y] != mountains[x][y]:
                    adjacentMountains[regionCounter].append(mountains[x + dx][y])
                # otherwise add to region and check neighbours 
                elif (x + dx, y) not in visited:
                    bfs((x + dx, y))
        # check up and down
        for dy in [-1, 1]:
            if 0 <= y + dy < GRID_SIZE:
                if mountains[x][y + dy] != mountains[x][y]:
                    adjacentMountains[regionCounter].append(mountains[x][y + dy])
                elif (x, y + dy) not in visited:
                    bfs((x, y + dy))
        
    # go through each mountain and add to a region
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            current = (i, j)
            if current not in visited:
                regions[regionCounter] = []
                adjacentMountains[regionCounter] = []
                bfs(current)
                regionCounter += 1 
    
    return regions, adjacentMountains 

def getPeaks(regions,adjacentMountains):
    peaks = 0
    for region in regions:
        isPeak = True
        height = regions[region][0]
        size = len(regions[region])
        
        # if any mountain adjacent to region is taller, then the region is not a peak
        for adjacent in adjacentMountains[region]:
            if adjacent > height:
                isPeak = False 
                break 
        if isPeak:
            peaks += size
    
    return peaks


def main():
    GRID_SIZE = 200
    mountains = []
    # read in data to 2d array
    with open('himalayas.txt', 'r') as f:
       for _ in range(GRID_SIZE):
           line = f.readline()
           row = list(map(int, line.split()))
           mountains.append(row)


    # group contiguous regions and track the mountains adjacent to them
    regions, adjacentMountains = getRegions(mountains, GRID_SIZE)
    # calculate number of peak mountains
    peaks = getPeaks(regions, adjacentMountains)
    
    print(peaks)
if __name__ == "__main__":
    main()
    
    