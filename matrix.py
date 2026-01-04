class Matrix:
    def __init__(self, n_rows, n_cols):
        self.nrows = n_rows
        self.ncols = n_cols

        self._matrix = [[0] * n_cols for n in range(n_rows)]

    def _getcols(self, col_index):
        return [x[col_index] for x in self._matrix]

    def __getitem__(self, key):
        self._check_bounds(key)
        if isinstance(key, tuple):
            row, col = key
            return self._matrix[row][col]
        else:
            return self._matrix[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            row, col = key
            if isinstance(value, int) or isinstance(value, float):
                self._check_bounds(key)
                self._matrix[row][col] = value
            else:
                raise ValueError("A numeric type was expected")
        else:
            if isinstance(value, list):
                if len(value) == self.ncols:
                    self._matrix[key] = value
                else:
                    raise ValueError("Not enough columns")
            else:
                raise ValueError("A List Type was expected")

    def _check_bounds(self, key):
        if isinstance(key, tuple):
            row, col = key
            if not (0 <= row < self.nrows and 0 <= col < self.ncols):
                raise IndexError("Index is out of Range")
            else:
                return
        elif isinstance(key, float) or isinstance(key, int):
            if not (0 <= key < self.nrows):
                raise IndexError("Index is out of Range")

    def __add__(self, other):
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrix must have similar dimensions do be added together")
        result = Matrix(self.nrows, self.ncols)
        for row in range(self.nrows):
            for col in range(self.ncols):
                result[row, col] = self[row, col] + other[row, col]

        return result
    
    def __sub__(self, other):
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrix must have similar dimensions do be added together")
        result = Matrix(self.nrows, self.ncols)
        for row in range(self.nrows):
            for col in range(self.ncols):
                result[row, col] = self[row, col] - other[row, col]        

        return result

    def __mul__(self, other):
        result = Matrix(self.nrows, self.ncols)
        if isinstance(other, int) or isinstance(other, float):
            for row in range(self.nrows):
                for col in range(self.ncols):
                    result[row, col] = self[row, col] * 3
        elif isinstance(other, Matrix):
            if self.ncols != other.nrows:
                raise ValueError("Rows and Columns must be equal for matrix multiplication")
            else:
                for i in range(self.nrows):
                    row = self._matrix[i]

                    for j in range(other.ncols):
                        col = other._getcols(j)
                        result[i, j] = sum(row[k] * col[k] for k in range(len(row)))
        
        return result
    
    def __rmul__(self, other):
        return self * other
    
    def __str__(self):
        matrix = self._matrix
        result = []
        for i in range(len(matrix)):
            result.append(f"{"".join(str(matrix[i]))}")

        return "\n".join(result)
    
matrix1 = Matrix(3, 3)
matrix2 = Matrix(3, 3)

matrix1[0] = [1, 8, 2]
matrix1[1] = [3, 6, 9]
matrix1[2] = [0, 2, 8]

matrix2[0] = [8, 2, 6]
matrix2[1] = [1, 8, 9]
matrix2[2] = [7, 4, 5]

matrix1[2, 0] = 8

print(matrix1)
print("-----------------------")
print(matrix2)
print("-----------------------")
print(matrix1 * matrix2)