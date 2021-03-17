def threeSumClosest( nums,target) :
        nums.sort()
        left = 0
        right = len(nums)-1
        sums_of_3 = []
        for i in range(1,len(nums)):
            while left < target:
                if nums[left] + nums[right + nums[i]] > target:
                    sums_of_3.append(nums[left] + nums[right + nums[i]])
                    right -= 1
                elif nums[left] + nums[right + nums[i]] < target:
                    sums_of_3.append(nums[left] + nums[right + nums[i]])
                    left +=1
        sums_of_3.sort()
        return sums_of_3[target]
print(threeSumClosest([1,-4,-1,3,0],1))

# total = nums[0] + nums[1] + nums[len(nums)-1]
# # print("total is calculated as the follows: ", nums[0], nums[1], nums[len(nums)-1])
# for i in range(len(nums)-2):
#             low = i + 1
#             high = len(nums) - 1
#             while low < high:
#                 curr = nums[i] + nums[low] + nums[high]
#                 # print("curr is calculated as the follows:", nums[i], nums[low], nums[high])
#                 if abs(target - curr) < abs(target - total):
#                     total = curr
#                 if curr < target:
#                     low += 1
#                     while low < high and nums[low] == nums[low-1]:
#                         low += 1
#                 elif curr > target:
#                     high -= 1
#                     while low < high and nums[high] == nums[high+1]:
#                         high -= 1
#                 else:
#                     return target
