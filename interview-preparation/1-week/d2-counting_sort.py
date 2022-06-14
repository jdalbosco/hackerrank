def counting_sort(numbers):
    frequency = [0]*100

    for number in numbers:
        frequency[number] += 1
    
    return frequency