def lonely_integer_v1(numbers):
    viewed = set()
    
    for n in numbers:
        if n in viewed:
            viewed.remove(n)
        else:
            viewed.add(n)
    
    return list(viewed).pop()
    
    
def lonely_integer_v2(numbers):
    numbers.sort()
    
    while len(numbers) > 1:
        n1, n2 = numbers.pop(), numbers.pop()
        if n1 != n2:
            return n1
    
    return numbers.pop()