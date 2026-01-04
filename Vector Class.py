class Vector:
    def __init__(self, data):
        if isinstance(data, int):
            self._coord = [0] * data
        elif isinstance(data, list):
            self._coord = data

    def __len__(self):
        return len(self._coord)
    
    def __getitem__(self, ind):
        return self._coord[ind]
    
    def __setitem__(self, ind, val):
        self._coord[ind] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Lengths of vectors must be equal")
        result = Vector(len(self))

        for ind in range(len(self)):
            result[ind] = other[ind] + self[ind]

        return result
    
    def __radd__(self, other):
        return self + other
    
    def __mul__(self, other):
        result = Vector(len(self))
        if isinstance(other, int):
            for x in range(len(self)):
                result[x] = self[x] * other
            
            return result
        
        elif isinstance(other, Vector) or isinstance(other, list):
            if len(self) != len(other):
                raise ValueError("Length of Vectors must be equal")
            for x in range(len(self)):
                result[x] = self[x] * other[x]
            
            return result.sum()
    
    def __eq__(self, other):
        return self._coord == other._coord
    
    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"<{str(self._coord[:])}>"
    
    def sum(self):
        result = 0
        for x in self:
            result += x
        
        return result

    
u = Vector([7, 3, 4, 8])
v = [3, 2, 9, 5] + u

print(u)
print(v)
print(u * v)
print(u * 3)
    
# vec_one = Vector(3)

# vec_one[1] = 3
# vec_one[0] = 4

# # print(vec_one)

# vect_two = vec_one + vec_one
# # print(vect_two)

# class listIterator:
#     def __init__(self, sequence):
#         self._seq = sequence
#         self._k = -1

#     def __next__(self):
#         self._k += 1

#         if self._k >= len(self._seq):
#             raise StopIteration("You've reached the end of the iterator")
#         else:
#             return self._seq[self._k]
        
#     def __len__(self):
#         return len(self._seq)
    
#     def __getitem__(self, ind):
#         return self[ind]
        
#     def __iter__(self):
#         return self
    

class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
        
    def __iter__(self):
        return self
    
    def printn_progressions(self, n):
        return " ".join(str(next(self)) for j in range(n))
    
class ArithmeticProgression(Progression):
    def __init__(self, start=0, increment=1):
        super().__init__(start)

        self._increment = increment

    def _advance(self):
        self._current += self._increment

arith = ArithmeticProgression(3, 4)
print(arith.printn_progressions(10))

class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._next = second

    def _advance(self):
        self._current, self._next = self._next, self._next + self._current

fibonacci = FibonacciProgression(3, 9)

print(fibonacci.printn_progressions(10))