# punched cards
def solve(R, C):
    rows  = 2*R + 1
    columns = 2 * C + 1
    
    for r in range(rows):
        line = ""
        #row borders
        if r % 2 == 0:
            #top row
            if r == 0:
                line = "..+"
            else:
                line = "+-+"
            line += "-+" * (C - 1)
        else:
            #second row
            if r == 1:
                line = "..|"
            else:
                line = "|.|"
            line += ".|" * (C - 1)
        print(line)
                


def main():

    T = int(input())
    for i in range(T):
        line = input()
        R, C = map(int, line.split())
        print("Case #{}:".format(i + 1))
        solve(R, C)

if __name__ == "__main__":
    main()