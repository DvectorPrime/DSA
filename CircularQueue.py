class CircularQueue:
    class Node:
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    def __init__(self):
        self._tail = None
        self._n = 0

    def __len__(self):
        return self._n
    
    def is_empty(self):
        return self._n == 0
    
    def first(self):
        if self.is_empty():
            raise ValueError("Empty Eque")
        
        return self._tail._next._element
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        
        front = self._tail._next

        if self._n == 1:
            self._tail = None
        else:
            self._tail._next = front._next

        self._n -= 1

        return front._element
    
    def enqueue(self, element):
        newest = self.Node(element, None)

        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest

        self._tail = newest
        self._n += 1

    def rotate(self):
        if self._n > 1:
            self._tail = self._tail._next

queue = CircularQueue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue.dequeue())
print(queue.dequeue())
print(len(queue))
print(queue.first())
queue.rotate()
print(queue.first())