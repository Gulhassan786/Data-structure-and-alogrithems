# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

def isPalindrome(x):
        var = str(x)
        
        if len(var) == 1:
            return True
        
        ptr1 = 0
        ptr2 = len(var)-1
        
        while ptr1 < ptr2:
            
            if var[ptr1] != var[ptr2]:
                return False
            
            ptr1 +=1
            ptr2 -=1
            
        return True

print(isPalindrome(1221))
