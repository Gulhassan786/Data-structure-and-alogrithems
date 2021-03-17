"""Problem Statement: Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter."""


def FindAnagrams(string1, string2):
      dic1 = {}
  dic2={}
  result=[]
  window_start=0
  for ch in string1:
      if ch in dic1:
          dic1[ch] += 1
      else:
          dic1[ch]=1
  for i in range(len(string2)):
    char=string2[i]
    if char not in dic2:
      dic2[char] = 0
    dic2[char] += 1
    if i >= len(string1):
      char=string2[window_start]
      if dic2[char] == 1:
        del dic2[char]
      else:
        dic2[char] -= 1
      window_start+=1
    if dic1 == dic2:
      result.append(window_start)
  return result
s= "cbaebabacd"
p= "abc"
print(FindAnagrams(p,s))
