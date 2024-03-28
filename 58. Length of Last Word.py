def lengthOfLastWord(s):
        if len(s) == 1 and ord(s) != 32:
            return 1
        
        length = 0
        pointer = len(s)-1
        # loop will not stop until we break it 
        while True:
            
            # checking if values is space and length is 0 it means we are at the end
            # of string and there is space so move pointer to left
            if ord(s[pointer]) == 32 and length <= 0:
                pointer -= 1
            
            #if there is value instead of space then add 1 to length
            else: 
                    length += 1
                    pointer -= 1

                    #if pointer is reached the end means there are no more char in string
                    # then break the loop
                    if pointer == -1 : break
                    
                    # we got space once again it means we have counted the length of
                    #last word in the string so break the loop
                    elif ord(s[pointer]) == 32:
                        break

        return length


output = lengthOfLastWord("qhahdfhdf")
print(output)