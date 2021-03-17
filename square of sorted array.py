def sortedSquares(nums):
        left = 0
        right = len(nums)-1
        square_list = []
        while left < right:
            print("hi")
            if nums[left]**2 > nums[right]**2:
                square_list.append(nums[left]**2)
                left += 1
            elif nums[left]**2 < nums[right]**2:
                square_list.append(nums[right]**2)
                right -= 1
        if left == right:
            square_list.append(nums[left]**2)
        square_list.sort()
        return square_list
