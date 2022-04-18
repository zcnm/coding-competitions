#template
def solve(field, N, K):
    fuel = 0
    final = 0
    
    for i in range(len(field) - 1):
        if field[i] > K:
            fuel += field[i] - K 
            field[i + 1] += field[i] - K 
    final = field[-1]
    if final > K:
        a0 = final % K
        aN = final - K 
        M = final // K 
        series = (a0 * M) + K * (M*(M-1))// 2
        fuel += series
    
    return fuel
        
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
    N, K = map(int, input().split())
    
    field = list(map(int, input().split()))
    ans = solve(field, N, K)
    print(ans)
    return 
if __name__ == "__main__":
    main()