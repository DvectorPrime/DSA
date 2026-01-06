from DoublyLinkedList import _DoublyLinkedList

class LinkedDeque(_DoublyLinkedList):

    def __init__(self):
        super().__init__()
    
    def first(self):
        if self._is_empty():
            raise ValueError("Deque is empty")
        
        return self._header._next._element
    
    def last(self):
        if self._is_empty():
            raise ValueError('Deque is empty')
        
        return self._trailer._prev._element
    
    def insert_first(self, element):
        return self._insert_between(element, self._header, self._header._next)
    
    def insert_last(self, element):
        return self._insert_between(element, self._trailer._prev, self._trailer)
    
    def delete_first(self):
        if self._is_empty():
            raise ValueError("Deque is empty")
        
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self._is_empty():
            raise ValueError('Deque is empty')
        
        return self._delete_node(self._trailer._prev)
    

deque1 = LinkedDeque()

deque1.insert_first(1)
deque1.insert_last(3)
deque1.insert_first(2)
deque1.insert_first(5)
deque1.insert_last(6)

print(deque1.first())
print(deque1.last())
print("-------------------------")

deque1.delete_first()
deque1.delete_last()
print(deque1.first())
print(deque1.last())
print("-------------------------")