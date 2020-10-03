"""
WAP that implements a Matrix class and performs addition, multiplication, and transpose operations on 3 x 3 matrices.
"""
class Matrix:
    def __init__(self):
        w,h = 3,3
        w, h = 8, 5;
        self._val = [[0 for x in range(w)] for y in range(h)]

    def updateMatrix(self):
        print('')
        print('Enter values for a 3x3 matrix')
        for i in range(0,3):
            for j in range(0,3):
                print('Enter value - mat[', i, '][', j,'] = ')
                self._val[i][j] = int(input())

    def add(self, mat):
        return

    def multiply(self, mat):
        ret = Matrix()
        for i in range(len(self._val)):
            for j in range(len(mat._val[0])):
                for k in range(len(mat._val)):
                    ret._val[i][j] += self._val[i][k] * mat._val[k][j]
        return ret

    def transpose(self):
        return

    def printMatrix(self):
        for i in range(0,3):
            print('')
            for j in range(0,3):
                print(' mat[', i, '][', j,'] = ', self._val[i][j], end='')
        print('')

matrix = Matrix()
matrix.updateMatrix()
print('=== Matrix 1 ===')
matrix.printMatrix()

matrix2 = Matrix()
matrix2.updateMatrix()
print('=== Matrix 2 ===')
matrix2.printMatrix()

matrix3 = matrix.multiply(matrix2)
print('=== Product of matrix 1 and matrix 2 ===')
matrix3.printMatrix()
