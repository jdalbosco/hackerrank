def is_too_chaotic(queue):
    for position, sticker_number in enumerate(queue):
        distance_from_original_position = sticker_number - (position + 1)
        if distance_from_original_position > 2:
            return True
    return False

    
def get_n_of_bribes(queue):
    bribes = 0
    switched = True
    
    while switched:
        switched = False
        for i in range(len(queue) - 1):
            if queue[i] > queue[i+1]:
                queue[i], queue[i+1] = queue[i+1], queue[i]
                bribes += 1
                switched = True

    return bribes
    
    
def minimum_bribes(q):
    if is_too_chaotic(q):
        print("Too chaotic")
    else:
        print(get_n_of_bribes(q))