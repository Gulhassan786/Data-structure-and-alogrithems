"""Problem Statement: Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string."""



# def checkInclusion(string1,string2):
#       dic1={}
#       dic2={}
#   window_start=0
#   for ch in string1:
#       if ch in dic1:
#           dic1[ch] += 1
#       else:
#           dic1[ch]=1
#   for i in range(len(string2)):
#     char=string2[i]
#     if char not in dic2:
#       dic2[char] = 0
#     dic2[char] += 1
#     if i >= len(string1):
#       char=string2[window_start]
#       if dic2[char] == 1:
#         del dic2[char]
#       else:
#         dic2[char] -= 1
#       window_start+=1
#     if dic1 == dic2:
#       return True
#   return False
# string1 = "ab" 
# string2 = "eidbaooo"
# print(checkInclusion(string1,string2))
