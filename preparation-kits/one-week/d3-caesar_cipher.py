ASCII_A = ord("A")
ASCII_Z = ord("Z")
ASCII_a = ord("a")
ASCII_z = ord("z")
ALPHABET_SIZE = ASCII_Z - ASCII_A

def caesar_cipher(message, offset):
    offset = offset % (ALPHABET_SIZE + 1)
    
    for i in range(len(message)):
        char = ord(message[i])
        ciphered_char = char
        
        if char >= ASCII_A and char <= ASCII_Z:
            ciphered_char = char + offset
            if ciphered_char > ASCII_Z:
                ciphered_char = ASCII_A + (ciphered_char % ASCII_Z) - 1
        
        if char >= ASCII_a and char <= ASCII_z:
            ciphered_char = char + offset
            if ciphered_char > ASCII_z:
                ciphered_char = ASCII_a + (ciphered_char % ASCII_z) - 1
        
        message = f"{message[:i]}{chr(ciphered_char)}{message[i+1:]}"
    
    return message