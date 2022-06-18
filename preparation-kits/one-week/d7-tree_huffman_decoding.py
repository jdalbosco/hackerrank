GO_LEFT = '0'
GO_RIGHT = '1'

def decode_huff(root, str_to_decode):
    def decode(root, idx):
        if root.left is None and root.right is None:
            return root.data, idx
        if str_to_decode[idx] == GO_LEFT:
            return decode(root.left, idx+1)
        elif str_to_decode[idx] == GO_RIGHT:
            return decode(root.right, idx+1)
    
    decoded = ""
    idx = 0
    
    while idx < len(str_to_decode):
        char, idx = decode(root, idx)
        decoded += char
        
    print(decoded)