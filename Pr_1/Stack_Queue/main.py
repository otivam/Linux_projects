class Stack:
    def __init__(self):
        self.items = []
         
    def is_empty(self):
        return self.items == []
        
    def push(self, item):
        self.items.insert(0,item)
        
    def pop(self):
        return self.items.pop(0)
        
    def print_stack(self):
        print(self.items)
        
s = Stack()
s.push("Gincho")
s.push("Megi")
s.print_stack()
s.pop()
s.print_stack()
print(s.is_empty())
s.print_stack()
s.pop()
print(s.is_empty())



class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        self.items.pop()
        
    def print_queue(self):
        print(self.items)
        
q = Queue()

q.enqueue("Gincho")
q.enqueue("Megi")
q.print_queue()
q.dequeue()
q.print_queue()
print(q.is_empty())
q.dequeue()
q.print_queue()
print(q.is_empty())