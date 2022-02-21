# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.



class Matrix():

    def __init__(self, m):
        self.m = m

    def __str__(self):
        matrix_strings = ''
        for el in range(len(self.m)):
            matrix_strings = matrix_strings + '\t'.join(map(str, self.m[el])) + '\n'
        return matrix_strings

    def __add__(self, other):
        add_matrix_result = list.copy(self.m)
        for el in range(len(self.m)):
            for param in range(len(self.m[el])):
                add_matrix_result[el][param] = self.m[el][param] + other.m[el][param]
        return Matrix(add_matrix_result)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

