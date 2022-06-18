def pairs(diff, numbers_arr):
    numbers_set = set(numbers_arr)
    pairs = 0
    
    for number in numbers_arr:
        if number - diff in numbers_set:
            pairs += 1
    
    return pairs