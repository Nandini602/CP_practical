def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)
    n = len(matrix[0])

    row = 0
    col = n - 1

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16

print(searchMatrix(matrix, target))
# Output: True
