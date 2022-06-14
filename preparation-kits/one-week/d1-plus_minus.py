def plus_minus(numbers):
    positives = 0
    negatives = 0
    zero = 0
    
    for number in numbers:
        if number > 0:
            positives += 1
        elif number < 0:
            negatives += 1
        else:
            zero += 1
    
    total_numbers = len(numbers)
    print("{:.6f}".format(positives/total_numbers))
    print("{:.6f}".format(negatives/total_numbers))
    print("{:.6f}".format(zero/total_numbers))