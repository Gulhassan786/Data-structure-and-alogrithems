"""Problem Statement:Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s"""


def longestOnes(array_, K):
    zero = 0
    result = 0
    window_Start = 0
    window_End = 0
    while window_End < len(array_):
        if array_[window_End] == 0:
            zero += 1
        while zero > K:
            if array_[window_Start] == 0:
                zero -= 1
            window_Start += 1
        result = max(result, window_End-window_Start+1)
        window_End += 1
    return result


Array = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2
print(longestOnes(Array, K))
