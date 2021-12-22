"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

def searchRange(nums, target):
    
    # Time complexity is O(log N)
    # Space complexity is O(1)
  
     result = [-1, -1]
     start = 0
     end = len(nums) - 1
     middle = (end + start) // 2
        
     while start <= end:
            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                if nums[start] == target and nums[end] == target:
                    result = [start, end]
                    break
                if nums[start] < target:
                    start += 1
                if nums[end] > target:
                    end -= 1
            middle = (end + start) // 2
     return result

# ========================================================================================================
          # Time complexity is O(N)
          # Space complexity is O(1)
        
        # Created list for storing index or starting and eding target       
        # result = []
        
        # # Checking if there is nothing in nums it means there is no target value so will return [-1,-1]
        # if len(nums) == 0 :
        #     return [-1, -1]
        # # Checking if nums has 1 value and that is euqals to target then we will return position of that
        # # value twice
        # elif len(nums) == 1 and nums[0] == target:
        #     return [0,0]
        # # Checking if nums has 1 value and that is not equals to target then we will return [-1, -1]
        # elif len(nums) == 1 and nums[0] != target:
        #     return[-1,-1]
        
        # for i in range(len(nums)):
        #     # if at particular index  from nums list value is equals to target then go ahead
        #     if nums[i] == target:

        #         """
        #         If result contain 2 index and we found another value matcing to target then we will remove 
        #         last value from resutl and insert new index value inplace of removed value because if we have 
        #         another value which is equals to target it means that last index value in result in not ending 
        #         index so,we need starting and eding index of target value from nums list. 
        #         """
        #         if len(result) == 2:
        #             result.pop()
        #             result.append(i)
        #         else:
        #             result.append(i)
        #  # If there is no value which is equals to target the we will return [-1,-1]           
        # if len(result) == 0:
        #     return [-1,-1]
        # # if there is only one value which is equals to target then we will return its index twice [0,0]
        # if len(result) == 1:
        #     return [result[0], result[0]]
        
        # return result
# ======================================================================================================

num = [1,2,8,8,8,9,10]
target = 2
print(searchRange(num, target))
