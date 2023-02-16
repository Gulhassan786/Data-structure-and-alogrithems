
def countGoodSubstrings(s):
        # Created 3 variables start and end for sliding window and counter to count of good strings
        counter = 0
        start = 0
        end = 1
        
        # checking if length of string is 2 or less then it the simple return 0 because good substring should be length 3
        if len(s) <= 2:
            return 0

        # Countinue loop until end is not greater than length of string [len(s)]
        while end <= len(s)-1:

            # if end is 1 [means starting point] and character at start and character at end index of string is not same increment 1 in end
            if end == 1 and s[start] != s[end]:
                end +=1
            
            # checking start char must not match char at end and end char not match char previous then end which is end-1 and char at start also must not match to char a head of start which can be written in two ways (start+1 or end-1) [this condition ensures that 3 characters are different from each other so its good sub string]
            elif s[start] != s[end] and s[end] != s[end-1] and s[start] != s[start+1]:
                # add one to counter means we found one good sub and also move window a head
                counter +=1 
                end +=1
                start += 1

            # if char at start and end are same at intial point just slide right corner a head by one  
            elif s[start] == s[end] and end == 1:
                end += 1
            
            # if we not found good sub str slide window a head
            else:
                end +=1 
                start += 1

        # At the end we will return how many good sub strings are their
        return counter
                

output = countGoodSubstrings("xyzzaz")
print(output)

# time complexity is O(n) and space complexity is O(1)

