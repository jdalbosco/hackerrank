# With a little help from my friends

ENQUEUE = "1"
DEQUEUE = "2"
PRINT   = "3"

class Queue:
    def __init__(self):
        self.stack = []
        self.reverse_stack = []
        
    def __move_to_reverse_stack(self):      
        while self.stack:
          self.reverse_stack.append(self.stack.pop())
            
    def enqueue(self, x):
        self.stack.append(x)
        
    def dequeue(self):
        if not self.reverse_stack:
          self.__move_to_reverse_stack()
        self.reverse_stack.pop()
        
    def print_first(self):
        if not self.reverse_stack:
            self.__move_to_reverse_stack()
        first = self.reverse_stack.pop()
        print(first)
        self.reverse_stack.append(first)
        

if __name__ == '__main__':
    queue = Queue()
    queries = int(input().strip())
    
    for _ in range(queries):
        query = input().strip()
        
        if query[0] == ENQUEUE:
            number = int(query[1:])
            queue.enqueue(number)
        elif query == DEQUEUE: queue.dequeue()
        elif query == PRINT: queue.print_first()
