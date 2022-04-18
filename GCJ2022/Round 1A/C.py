# Weight Lifting
def solve(weights, W):
    total = 0
         


def main():

    T = int(input())
    for i in range(T):
        weights = []
        E, W = map(int, input().split())
        for _ in range(E):
            weight = list(map, int, input().split())
            weights.append(weight)
        answer = solve(weights, W)
        print("Case #{}: {}".format(i + 1, answer))

if __name__ == "__main__":
    main()