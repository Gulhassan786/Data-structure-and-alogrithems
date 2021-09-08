"""" 
Given a zero-based permutation nums (0-indexed),
 build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
"""

def buildArray(nums):
    answer = []
    # checking if the lenght of an array is 1 simply return it
    if len(nums) == 1:
        return nums
    #inserting the elements in ans array
    for i in range ( len(nums)):
        answer.append(nums[nums[i]])

Array = [1,2,4,6,5,3]
print(buildArray(Array))