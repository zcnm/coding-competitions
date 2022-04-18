#template
def solve(N):
    layers = []
    for i in range(N):
        if i == 0:
            layers.append(1)
        elif i % 5 == 0:
            layers.append(layers[-1] + 6)
        else:
            layers.append(layers[-1] + 3)
        
    width = layers[-1]
    for i in range(len(layers)):
        layer = layers[i]
        padding = (width - layer) // 2
        if i % 5 == 0:
            character = "-"
        else:
            character = "#"
        
        line = "." *  padding + character * layer + "." * padding
        print(line)
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
    solve(N)
    return 
if __name__ == "__main__":
    main()