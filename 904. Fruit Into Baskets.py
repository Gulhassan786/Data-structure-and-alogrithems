#Medium level problem

def totalFruit( tree):
        import collections
        l, nums, res = 0, collections.Counter(), 0
        for r in range(len(tree)):
            nums[tree[r]] += 1
            while len(nums) > 2:
                nums[tree[l]] -= 1 
                if not nums[tree[l]]:
                    nums.pop(tree[l])
                l += 1
            res = max(res, r - l + 1)
        print(res)



lst = [1,2,3,1,1,2,2]
totalFruit()