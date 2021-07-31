# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.


def firstUniqChar(s):
        dic = {}

        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] = -1
            else:
                dic[s[i]] = i

        # print(dic)
        for i in dic:
            if dic[i] >= 0:
                return dic[i]
        return -1

print(firstUniqChar("gulHassan"))
