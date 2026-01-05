class LinkedStack:
    class Node:
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._n = 0

    def __len__(self):
        return self._n
    
    def is_empty(self):
        return self._n == 0
    
    def push(self, element):
        current = self.Node(element, self._head)

        self._head = current
        self._n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is Empty")
        
        answer = self._head._element

        self._head = self._head._next
        self._n -= 1

        return answer
    
    def top(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._head._element
    

stack = LinkedStack()

stack.push(3)
stack.push(5)
stack.push(8)
stack.push(4)

print(stack.pop())
print(len(stack))
print(stack.top())