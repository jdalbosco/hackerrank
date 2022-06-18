def preorder_string(root):
    string = ''
    if root == None:
        return string
    string += str(root.info) + ' '
    string += preorder_string(root.left)
    string += preorder_string(root.right)
    return string
    
def preorder(root):
    print(preorder_string(root))