#template
""" 
binary search to find max time to reach destination
using Breadth First Search pathfinding algorithm
"""
def solve(V, connections, low, high):
    home = 1
    # default answer if no path is found
    latest = -1
    
    # bfs for destination
    def isPossible(curr, time):   
        # stop if we found the destination
        if curr == V:
            return True 
        # get all possible paths from current location and time
        paths = [connection[0] for connection in connections[curr] if connection[1] > time]
        
        # if there are none then we are stuck
        if len(paths) == 0:
            return False
        
        # if any path exists to get to destination return true
        for path in paths:
            if isPossible(path, time + 1):
                return True 
        return False
    
    # binary search to get max time
    while low < high:
        time = (high + low) // 2
        if isPossible(home, time):
            low = time + 1
            if time > latest:
                latest = time 
        else:
             high = time
             
        if isPossible(home, low):
            if low > latest:
                latest = low 
    
    return latest
    
    
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
    connections = {}
    minTime = 10**9
    maxTime = 0
    V, E = map(int,input().split())
    for i in range(E):
        start, end, time = map(int,input().split())
        # if the time is 0 can never use the path so ignore
        if time == 0:
            continue
        # track highest and lowest time
        if time < minTime:
            minTime = time
        if time > maxTime:
            maxTime = time 
         
        # read paths into dictionary
        # each connection is two way   
        if start not in connections:
            connections[start] = []
        connections[start].append((end, time))
        
        if end not in connections:
            connections[end] = []
        connections[end].append((start, time))
        
    # -1 from min and max time since can only use path if at least -1 time before it
    ans = solve(V, connections, minTime - 1, maxTime - 1)
    print(ans)
    return 
if __name__ == "__main__":
    main()