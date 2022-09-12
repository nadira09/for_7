# task 1

class Matrix:
    def __init__(self, list1):
        self.list1 = list1

    def __add__(self, other):
        matrix = [[0, 1, 0], [2, 3, 0], [4, 5, 0]]
        list = len(self.list1)
        a = ''

        for i in range(list):
            for j in range(len(self.list1[i])):
                matrix[i][j] = self.list1[i][j] + other.list1[i][j]
            a += f'{matrix[i]}\n'
        return a

    def __str__(self):
        return f'{self.list1}'

mat1 = Matrix([[0, 1, 0], [2, 3, 0], [4, 5, 0]])
mat2 = Matrix([[0, 1, 0], [2, 3, 0], [4, 5, 0]])
print(mat1 + mat2)

# task 2

from abc import ABC, abstractmethod

class CS(ABC):
    def __init__(self, H):
        self.H = H

    @abstractmethod
    def consumption(self):
        return

    def __str__(self):
        return str(self.H)

class C(CS):
    @property
    def consumption(self):
        return self.H / 6.5 + 0.5

class S(CS):
    @property
    def consumption(self):
        return self.H * 2 + 0.3

a = C(4)
b = S(8)
print(a.consumption)
print(b.consumption)
print(a.consumption + b.consumption)

# task 3

class Cells:
    def __init__(self, counter):
        self.counter = counter

    def __add__(self, other):
        return Cells(self.counter + other.counter)

    def __sub__(self, other):
        if self.counter - other.counter > 0:
            return Cells(self.counter - other.counter)
        else:
            print('Отрицательное число')

    def __mul__(self, other):
        return Cells(self.counter * other.counter)

    def __truediv__(self, other):
        return Cells(self.counter // other.counter)

    def make_order(self, cells):
        a = ''

        for i in range(int(self.counter / cells)):
            a += f'{"*" * cells}\\n'
        return a

    def __str__(self):
        return f'Результат {self.counter}'

c1 = Cells(15)
c2 = Cells(5)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(5))
print(c2.make_order(5))





