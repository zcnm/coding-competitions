# d1000000
def solve(n, dice):
    dice.sort()
    current = 1
    for die in dice:
        if die >= current:
            current += 1
    return current - 1
    

def main():
    T = int(input())
    for i in range(T):
        numDice = int(input())
        line = input()
        
        dice = list(map(int, line.split()))
        ans = solve(numDice, dice)
        output = "Case #{}: {}".format(i + 1, ans)
        print(output)

if __name__ == "__main__":
    main()