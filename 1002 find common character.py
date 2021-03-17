""" Problem Statement: Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order."""
# Hash_table
def commonChars(A):
    dic = {}
    # Creating keys from the first string of list
    for x in A[0]:
        dic[x] = dic.get(x, 0) + 1

    # checking the presence of charcter in strings
    for x in dic:
        for i in range(1, len(A)):
            if x in A[i]:
                dic[x] = min(dic[x], A[i].count(x))

            # If charcter is not present in any string asign the 0 value to it's key
            else:
                dic[x] = 0
                break

    # Creating list of charcters which is present in all the string
    ans = []
    for k, v in dic.items():
        ans += v * [k]

    #  Returning the list which contain the list of charcters
    return ans

# Calling the function and passing the value to it
print(commonChars(["cool", "lock", "cook"]))
