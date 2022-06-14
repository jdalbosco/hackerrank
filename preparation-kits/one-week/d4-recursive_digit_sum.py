def super_digit(number, repeat=1):
    digits = [int(digit) for digit in list(number)]
    sum_of_digits = sum(digits) * repeat
    
    return sum_of_digits if sum_of_digits < 10 else super_digit(str(sum_of_digits))