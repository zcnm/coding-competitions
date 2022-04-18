#template

"""
    right slanted when i < j < k and mountains[j] > mountains[i] > mountains[k]
    mountain consists of left and right 'bases' and a peak in the middle
    every time we see an upwards slope relative to left base add to peaks 
    every time we see right base lower than left base, the number of mountains that use left base and that right base is the number of peaks we've seen
    
    left slanted can use same alg just going right to left through array
"""
def solve(mountains):
    N = len(mountains)
    leftSlanted = 0
    rightSlanted = 0
    # get right slanted mountains
    for i in range(N):
        peaks = 0
        for j in range(i + 1, N):
            if mountains[j] > mountains[i]:
                peaks += 1
            elif mountains[j] < mountains[i]:
                rightSlanted += peaks 
    
    #get left slanted mountains 
    #reverse mountains
    mountains = mountains[::-1]
    for i in range(N):
        peaks = 0
        for j in range(i + 1, N):
            if mountains[j] > mountains[i]:
                peaks += 1
            elif mountains[j] < mountains[i]:
                leftSlanted += peaks 
                
    return [leftSlanted, rightSlanted]
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
    N = int(input())
    
    mountains = list(map(int, input().split()))
    ans = solve(mountains)
    printArray(ans)
    return 
if __name__ == "__main__":
    main()