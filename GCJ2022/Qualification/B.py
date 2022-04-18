# 3D printing
def solve(printers):
    required = 10 ** 6
    colours = [min(colour) for colour in zip(*printers)]
    if sum(colours) < required:
        return ["IMPOSSIBLE"]
    
    current = 0
    output = []
    for colour in colours:
        if current + colour < required:
            current += colour
            output.append(colour)
        else:
            output.append(required - current)
            current = required 
    return output 
def main():

    T = int(input())
    for i in range(T):
        printers = []
        for j in range(3):
            line = input()
            colours = list(map(int, line.split()))
            printers.append(colours)
        solution = solve(printers)
        output = "Case #{}:".format(i + 1)
        for sol in solution:
            output += " " + str(sol)
        print(output)

if __name__ == "__main__":
    main()