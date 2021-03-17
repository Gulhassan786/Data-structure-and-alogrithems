"""  Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
 """
# Hash_table
def smallerNumbersThanCurrent(nums) :
        dic = {}
        for index, value in enumerate(sorted(nums)):
            if value not in dic:
                dic[value] = index

        ans = []
        for j in nums:
            if j in dic:
                ans.append(dic[j])
        return ans
print(smallerNumbersThanCurrent([8,1,2,2,3]))