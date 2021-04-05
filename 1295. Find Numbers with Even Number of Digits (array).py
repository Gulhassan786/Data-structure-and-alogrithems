""" Given an array nums of integers, return how many of them contain an even number of digits."""

def findNumbers(nums):
    count = 0
    for i in range(len(nums)):
        if len( str(nums[i]))%2 == 0:
            count +=1
    return count


Nums = [12, 345, 2, 6, 7896]
print(findNumbers(Nums))

print("Gul hassan")