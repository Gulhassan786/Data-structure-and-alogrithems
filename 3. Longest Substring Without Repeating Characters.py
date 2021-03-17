# Problem Statement: Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring( string):
        charSet = set()
        result = 0
        left_window = 0
        for right_window in range(len(string)):
            while string[right_window] in charSet:
                charSet.remove(string[left_window])
                left_window += 1
            charSet.add(string[right_window])
            result = max(result, right_window - left_window + 1)
        return result

print (lengthOfLongestSubstring("gulhassan"))