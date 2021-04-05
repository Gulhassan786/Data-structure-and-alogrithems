""" Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid."""

def countNegatives(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                count +=1
    return count


lst = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(countNegatives(lst))
