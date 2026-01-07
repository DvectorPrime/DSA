class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("must be implemented by subclass")
        
        def __eq__(self, value):
            raise NotImplementedError("must be implemented by subclass")
        
        def __ne__(self, value):
            return not (self == value)
        
    def root(self):
        raise NotImplementedError("must be implemented by subclass")
    
    def parent(self, p):
        raise NotImplementedError("must be implemented by subclass")
    
    def num_children(self, p):
        raise NotImplementedError("must be implemented by subclass")
    
    def children(self, p):
        raise NotImplementedError("must be implemented by subclass")
    
    def __len__(self):
        raise NotImplementedError("must be implemented by subclass")
    
    def is_root(self, p):
        raise NotImplementedError("must be implemented by subclass")
    
    def is_leaf(self, p):
        raise NotImplementedError("must be implemented by subclass")
    
    def is_empty(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))    
    
    def height(self, p=None):
        if p == None:
             p = self.root()

        return self._height(p)
    
class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError("must be implemented by subclass")
    
    def right(self, p):
        raise NotImplementedError("must be implemented by subclass")
    
    def sibling(self, p):
        parent = self.parent(p)

        if parent == None:
            return None
        elif self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)
        
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)