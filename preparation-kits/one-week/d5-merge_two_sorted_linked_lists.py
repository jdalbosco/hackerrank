# SinglyLinkedList() is given in the challenge.

def merge_lists(head_A, head_B):
    merged_list = SinglyLinkedList()
    head = merged_list
    
    def end_of_list_A():
        return head_A == None
    
    def end_of_list_B():
        return head_B == None
    
        
    while not end_of_list_A() and not end_of_list_B():
        value_A, value_B = head_A.data, head_B.data
        
        if value_A < value_B:
            merged_list.data = value_A
            head_A = head_A.next
        else:
            merged_list.data = value_B
            head_B = head_B.next
            
        merged_list.next = SinglyLinkedList()
        merged_list = merged_list.next
        
    if end_of_list_A():
        merged_list.data = head_B.data
        merged_list.next = head_B.next
        
    elif end_of_list_B():
        merged_list.data = head_A.data
        merged_list.next = head_A.next  
        
    return head