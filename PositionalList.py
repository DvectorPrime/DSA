from DoublyLinkedList import _DoublyLinkedList
class PositionalList(_DoublyLinkedList):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(self) is type(other) and other._node is self._node
        
        def __ne__(self, other):
            return not (self == other)
        
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("P is not a valid position")
        if p._container is not self:
            raise ValueError("P doesn't belong in this list")
        if p._node._next is None:
            raise ValueError("P is deprecated and no longer valid")
        
        return p._node