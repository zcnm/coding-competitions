# Pyramid Scheme
def volume(height):
    widths = [1]
    for level in range(2, height + 1):
        # every 5th layer after top width increases by 6
        if (level - 1) % 5 == 0:
            widths.append(widths[-1] + 6)
        # otherwise widths increase by 1
        else:
            widths.append(widths[-1] + 2)
    
    # sum volume of each layer
    vol = 0
    for width in widths:
        vol += width * width 
    return vol 

def main():
    print(volume(20))
    
if __name__ == "__main__":
    main()