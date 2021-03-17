"""Problem Statement: Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
In one operation, you can choose any character of the string and change it to any other uppercase English character.
Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.
Note:
Both the string's length and k will not exceed 104."""

def characterReplacement(string, k):
    window_Start = 0
    char_freq = {}
    maxlength = 0
    maxrepeatchar = 0
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        maxrepeatchar = max(maxrepeatchar, char_freq[right_char])
        if (window_end - window_Start + 1) - maxrepeatchar > k:
            left_char = string[window_Start]
            char_freq[left_char] -= 1
            window_Start += 1
        maxlength = max(maxlength, window_end - window_Start + 1)
    return maxlength

s = "AABABBA"
k = 2
print(characterReplacement(s, k))
