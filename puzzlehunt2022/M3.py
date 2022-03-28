# Fleeing Farmer

def decrypt(ciphertext, x, direction = 1):
    plainText = ""
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        # amount to shift letter up or down by  
        shift = x * (i + 1)
        
        """
        ord(letter) converts letter to number
        ord(a) = 97
        ord(b) = 98 
        ... etc
        
        chr(num) converts number back to letter 
        """
        
        # add shift to letter
        # mod 26 to loop around alphabet 
        # convert back to letter
        plainText += chr((ord(letter) + direction * shift - 97) % 26 + 97)
    return plainText

def main():
    ciphertext = "bmrefsqciwxyyrhfrxld"
    # try different values of x and different directions 
    for x in range(1, 8):
        print(decrypt(ciphertext, x, 1))
        print(decrypt(ciphertext, x, -1))
    
    print()
    # answer
    print(decrypt(ciphertext, 7, 1)) 
if __name__ == "__main__":
    main()