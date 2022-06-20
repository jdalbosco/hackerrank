def find_median(numbers):
    numbers.sort()
    median_idx = len(numbers)//2
    return numbers[median_idx]