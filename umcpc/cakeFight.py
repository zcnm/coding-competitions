#template
"""
Observations: 
- Optimal cake strategy when starting at cake i does not change regardless of any previous cake 
i.e. it does not matter what value of cake you currently have when you have the token, your strategy moving forwards remains constant

- both players will have the same optimal strategy when having token at cake i

- the amount of cake the opponent receives when the player performs the optimal strategy will be the total remaining cakes not picked up by the player
i.e the sum of cakes[i:] - amount of cake the player receives

- if you have the token at the final cake, you would always take it

Strategy:
work backwards starting from final cake 
1) always take final cake
2) giving the opponent a cake will allow you to perform the optimal move for the next cake
3) taking a cake will allow your opponent to perform the optimal move for the next cake, but will give you an amount of cake as compensation
4) most amount of cake received at a slice will equal to the max of the most amount of cake received at the next slice 
                        OR the current slice amount + total remaining cake - most amount of cake received at next slice 

"""
def solve(cakes):
    n = len(cakes) - 1
    # array holding sum of remaining cakes
    suffixSum = [sum(cakes)]
    for cake in cakes[:-1]:
        suffixSum.append(suffixSum[-1] - cake)
        
    # store optimal strategy at each slice
    dp = {}
    # always take final slice
    dp[n] = cakes[n]
    
    # looping backwards through cakes
    n -= 1
    while n >= 0:
        # taking a slice nets the current slice amount + whatever the opponent will leave you when following optimal strategy
        take = cakes[n] + suffixSum[n] - dp[n + 1]
        # giving a slice allows you to make optimal move next slice
        give = dp[n + 1]
        dp[n] = max(take, give)
        n -= 1
    
    # joe starts with token so he makes first move
    joe = dp[0]
    donald = suffixSum[0] - joe 
    return [donald, joe]
    
        
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
    cakes = list(map(int, input().split()))
    ans = solve(cakes)
    printArray(ans)
    return 
if __name__ == "__main__":
    main()