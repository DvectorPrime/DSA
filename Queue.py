class Queue:
    def __init__(self):
        self._in_stack = []
        self._out_stack = []
        self._size = 0

    def __len__(self):
         return self._size
    
    def is_empty(self):
        return self._size == 0 
    
    def _update_out_stack(self):
        while self._in_stack:
            self._out_stack.append(self._in_stack.pop())
    
    def enqueue(self, e):
        self._in_stack.append(e)
        self._size += 1

        print(self._in_stack, self._out_stack)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        
        if len(self._out_stack) == 0:
             self._update_out_stack()

        answer = self._out_stack.pop()
        self._size -= 1
        print(self._in_stack, self._out_stack)       
        return answer
        
    def first(self):
        if len(self._out_stack) == 0:
             self._update_out_stack()

        return self._out_stack[-1]


queue1 = Queue()

queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(1)
queue1.dequeue()
queue1.enqueue(4)
queue1.enqueue(5)
queue1.dequeue()
queue1.dequeue()
queue1.dequeue()
queue1.enqueue(6)