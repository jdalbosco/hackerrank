def flipping_matrix(matrix):
    quadrant_size = len(matrix)//2
    max_sum = 0

    for i in range(quadrant_size):
        for j in range(quadrant_size):
            neg_i = -(i+1)
            neg_j = -(j+1)
            max_sum += max(matrix[i][j], matrix[i][neg_j], matrix[neg_i][j], matrix[neg_i][neg_j])
    
    return max_sum