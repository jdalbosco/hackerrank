def diagonal_difference(matrix):
    left_to_right = 0
    right_to_left = 0
    
    for i in range(len(matrix)):
        left_to_right += matrix[i][i]
        right_to_left += matrix[i][-(i+1)]
    
    return abs(left_to_right - right_to_left)