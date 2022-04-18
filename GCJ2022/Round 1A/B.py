# Equal Sum


def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
def solve(powersOfTwo, rest):
    printArray(powersOfTwo +  rest)

    givenArray = list(map(int, input().split()))
    givenArray.sort(reverse = True)
    
    array1 = []
    array2 = []
    total1 = 0
    total2 = 0
    
    for num in givenArray:
        if total1 <= total2:
            array1.append(num)
            total1 += num 
        else:
            array2.append(num)
            total2 += num 
    for num in rest:
        if total1 <= total2:
            array1.append(num)
            total1 += num 
        else:
            array2.append(num)
            total2 += num 
    for num in powersOfTwo:
        if total1 <= total2:
            array1.append(num)
            total1 += num 
        else:
            array2.append(num)
            total2 += num 
    printArray(array1)
    return
    

def main():
    #preprocessing
    powersOfTwo = []
    for i in range(30):
        powersOfTwo.append(2**i)
    
    rest = []
    for j in range(10000, 10000 + 100 - 30):
        rest.append(j)
        
    rest.sort(reverse = True)
        
    powersOfTwo.sort(reverse = True)
    #------------------------------
    
    T = int(input())
    for i in range(T):
        N = int(input())
        solve(powersOfTwo, rest)

if __name__ == "__main__":
    main()