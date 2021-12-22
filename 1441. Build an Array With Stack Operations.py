"""
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

    Push: Read a new element from the beginning list, and push it in the array.
    Pop: delete the last element of the array.
    If the target array is already built, stop reading more elements.

Return the operations to build the target array. You are guaranteed that the answer is unique.
"""

def buildArray(target, n):
        
        result = []
        index = 0
        num = 1
        
        while num <= n:
            
            if index == len(target):
                return result
            
            elif target[index] == num:
                result.append("Push")
                index +=1
                
            elif target[index] != num:
                result.append("Push")
                result.append("Pop")
            
            num += 1
            
        return result

lst = [1,2,4,5,6,7]
num = 7

print(buildArray(lst,num))

# Time Complexity O(N)
# Sapce Complexity O(N)