# Double or One Thing
def solve(S):
    n = len(S)
    if n == 1:
        return S
    
    reverseString = S[-1]
    doubleLetter = False
    for i in range(1, n):
        j = n - i - 1 
        reverseString += S[j]
        if S[j] < S[j + 1]:
            reverseString +=  S[j]
            doubleLetter = True 
        elif S[j] == S[j + 1]:
            if doubleLetter: 
                reverseString += S[j]
        
        else:
            doubleLetter = False 
    return reverseString[::-1]
                        


def main():

    T = int(input())
    for i in range(T):
        line = input()
        y = solve(line)
        print("Case #{}: {}".format(i + 1, y))

if __name__ == "__main__":
    main()