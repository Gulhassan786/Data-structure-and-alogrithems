# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


def longestCommonPrefix(strs):

        common = []
        for l in strs[0]:
            if all(s.startswith("".join(common)+l) for s in strs):
                common.append(l)
            else:
                break
        return "".join(common)


  print(longestCommonPrefix( ["flower","flow","flight"]))