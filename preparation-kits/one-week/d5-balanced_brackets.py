IS_BALANCED = 'YES'
IS_NOT_BALANCED = 'NO'

OPENING_BRACKETS = '({['

def is_matching(opening, closing):
    if opening == '(': return True if closing == ')' else False
    if opening == '{': return True if closing == '}' else False
    if opening == '[': return True if closing == ']' else False

def is_balanced(string):
    brackets = []
    
    for char in list(string):
        if char in OPENING_BRACKETS:
            brackets.append(char)
        else:
            if not brackets:
                return IS_NOT_BALANCED
            opening = brackets.pop()
            if not is_matching(opening, char):
                return IS_NOT_BALANCED
                
    if brackets:
        return IS_NOT_BALANCED
    
    return IS_BALANCED