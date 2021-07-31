# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    sMap = {}
    tMap = {}
    p1 = 0
    p2 = len(s) - 1
    while p1 <= p2:

        if s[p1] not in sMap:
            sMap[s[p1]] = []
        sMap[s[p1]].append(p1)

        if p1 != p2:

            if s[p2] not in sMap:
                sMap[s[p2]] = []

            sMap[s[p2]].append(p2)

        if t[p1] not in tMap:
            tMap[t[p1]] = []
        tMap[t[p1]].append(p1)

        if p1 != p2:
            if t[p2] not in tMap:
                tMap[t[p2]] = []
            tMap[t[p2]].append(p2)

        if sMap[s[p1]] != tMap[t[p1]]:
            return False

        if sMap[s[p2]] != tMap[t[p2]]:
            return False

        p1 += 1
        p2 -= 1
    
    return True

print(isIsomorphic("foo","bar"))