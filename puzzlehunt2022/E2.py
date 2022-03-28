# Bazaar Thief

def main():
    with open('bazaar.txt', 'r') as f:
        lines = f.readlines()
    
    # read in numbers to list
    nums = []
    for line in lines:
        l = line.strip() # removes trailing \n character
        num = int(l)
        nums.append(num)
    
    nums.sort()
    print(nums)
    
    # -> [708, 715, 722, 729, 736, 743, 750, 757, 764, 771, 778, 785, 792, ...]
    # notice pattern: numbers are 7 apart
    
    for num in nums:
        # find num that does not follow pattern
        if (num - nums[0]) % 7 != 0:
            print(num)
    
if __name__ == "__main__":
    main()