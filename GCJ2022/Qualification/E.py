# Twisty little passages
#interactive
def solve(N, K):
    passages = {}
    seen = 0
    tDegrees = 0
    
    for i in range(N):
        passages[i] = 0

    for i in range(K):
        R, P = map(int, input().split())
        if passages[R - 1] == 0:
            if i % 2 == 0:
                seen += 1
                tDegrees += P
        passages[R - 1] = P 
        
        if i % 2 == 0:
            print("W")
        else: 
            seenAll = True 
            for cave in passages:
                if passages[cave] == 0:
                    seenAll = False 
                    print("T", cave + 1)
                    break 
            if seenAll:
                print("E", sum(passages.values()) // 2)
                return 
    
    R, P = map(int, input().split())
    if passages[R - 1] == 0:
        if K % 2 == 0:
            seen += 1
            tDegrees += P
    passages[R - 1] = P 
    
    averageDegree = tDegrees / seen 
    
    total = 0 
    for cave in passages:
        if passages[cave] == 0:
            total += averageDegree 
        else:
            total += passages[cave]
    
    estimate = int(total // 2)
    print("E", estimate)
    return

            

def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        solve(N, K)
if __name__ == "__main__":
    main()