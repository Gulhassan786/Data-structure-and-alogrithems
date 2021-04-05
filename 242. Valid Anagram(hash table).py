""" Given two strings s and t , write a function to determine if t is an anagram of s. """


def isAnagram(s, t):
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for j in t:
            if j in dic:
                dic[j] -= 1
            else:
                return False
        for v in dic.values():
            if v != 0:
                return False
        return True


print(isAnagram("anagram", "nagaram"))


