APPEND = "1"
DELETE = "2"
PRINT = "3"
UNDO = "4"

class TextEditor:
    def __init__(self):
        self.string = ""
        self.actions = []
        
    def __add_to_actions(self, op, string):
        self.actions.append((op, string))
        
    def append(self, str_to_append, is_undoing=False):
        self.string += str_to_append
        if not is_undoing:
            self.__add_to_actions(APPEND, str_to_append)
        
    def delete(self, k, is_undoing=False):
        self.string, str_to_delete = self.string[:-k], self.string[-k:]
        if not is_undoing:
            self.__add_to_actions(DELETE, str_to_delete)
        
    def print_char(self, k):
        print(self.string[k-1])
        
    def undo(self):
        op, string = self.actions.pop()
        if op == APPEND:
            self.delete(len(string), True)
        elif op == DELETE:
            self.append(string, True) 
            
            
if __name__ == '__main__':
    text_editor = TextEditor()
    queries = int(input().strip())
    
    for _ in range(queries):
        query = input().strip()
        op, content = query[0], query[2:]
        
        if op == APPEND: text_editor.append(content)
        elif op == DELETE: text_editor.delete(int(content))
        elif op == PRINT: text_editor.print_char(int(content))
        elif op == UNDO: text_editor.undo()