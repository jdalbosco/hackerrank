def remove_char_at_index(string, idx):
    return string[:idx] + string[idx+1:]

def is_palindrome(s):
    return s == s[::-1]

def palindrome_index(s):
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            if is_palindrome(remove_char_at_index(s, start)):
                return start
            elif is_palindrome(remove_char_at_index(s, end)):
                return end
        start += 1
        end -= 1
  
    return -1