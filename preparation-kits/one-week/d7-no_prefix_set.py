def validate_set(strings):
    accepted_strings = set()
    invalid_strings = set()
    
    def print_bad_set(string):
        print("BAD SET")
        print(string)

    for string in strings:
        if string in invalid_strings:
            print_bad_set(string)
            return
        
        substring = ''
        for char in string:
            substring += char
            if substring in accepted_strings:
                print_bad_set(string)
                return
            else:
                invalid_strings.add(substring)
        
        accepted_strings.add(string)
                
    print("GOOD SET")