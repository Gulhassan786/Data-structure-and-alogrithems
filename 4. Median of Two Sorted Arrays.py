""" Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays."""


def findMedianSortedArrays(nums1, nums2):
    # taking element from list two and inserting in list 1 (nums1)
    # for i in nums2:
    #     nums1.append(i)
    nums1+=nums2
    
    nums1.sort()
    
    mid = len(nums1)//2
    
    if len(nums1)%2 == 0:
        return  (nums1[mid]+nums1[mid-1])/2
    else:
        return nums1[mid]

n1 = [1,2]
n2 = [4,3]
print(findMedianSortedArrays(n1,n2))

# time: O(n log n)
# space: O(n)