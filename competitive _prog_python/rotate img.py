def rotate(matrix):
    n = len(matrix)
    layers = n // 2

    for layer in range(layers):
        for i in range(layer, n - layer - 1):
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[n - i - 1][layer]
            matrix[n - i - 1][layer] = matrix[n - layer - 1][n - i - 1]
            matrix[n - layer - 1][n - i - 1] = matrix[i][n - layer - 1]
            matrix[i][n - layer - 1] = temp

    return matrix

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# matrix2=[[2,3],[8,9]]
rotated2 = rotate(matrix2)
print(rotated2)
# Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]