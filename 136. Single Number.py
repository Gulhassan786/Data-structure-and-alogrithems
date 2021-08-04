"""  Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""
# Hash_tabel
def singleNumber(nums):
        dic = {}
        
        # Creating the keys and asigning the values to the keys
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        # Geting the vlaue and keys from the dictionary and checking if any key has value 1 return it
        for k, v in dic.items():
            if v == 1:
                return k
            
# Passing the argument to the funtion and printing it's returned value
print(singleNumber([8,2,3,2,3]))




# def singleNumber(nums):
#         # Cheking that if any value occurs only one time just return it
#         for i in nums:
#             if nums.count(i) == 1:
#                 return i

# # Passing the argument to the funtion and printing it's returned value
# print(singleNumber([8, 2, 3, 2, 3,8,9]))
print("Kali linux Os")
