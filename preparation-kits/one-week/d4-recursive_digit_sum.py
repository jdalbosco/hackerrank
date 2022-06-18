def super_digit(str_number, repeat=1):
    digits = [int(digit) for digit in list(str_number)]
    sum_of_digits = sum(digits) * repeat
    
    return sum_of_digits if sum_of_digits < 10 else super_digit(str(sum_of_digits))