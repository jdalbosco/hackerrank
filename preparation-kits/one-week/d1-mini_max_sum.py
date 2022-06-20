def mini_max_sum(numbers, length):
    numbers.sort()
    
    def mini_sum():
        mini_sum = 0
        for i in range(len(numbers) - length):
            mini_sum += numbers[i]
        return mini_sum
            
    def max_sum():
        max_sum = 0
        for i in range(length, len(numbers)):
            max_sum += numbers[i]
        return max_sum
    
    print(mini_sum(), max_sum())