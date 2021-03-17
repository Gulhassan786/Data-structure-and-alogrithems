
def moveZeroes(nums):
        if len(nums) <= 1:
            return nums
        nums.sort()
        left = right = 0
        while right < len(nums):
            if nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
        return nums
print(moveZeroes([2,1, 0, 3, 12]))
