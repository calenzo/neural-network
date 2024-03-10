import math
from random import random


class Matrix:
    def __init__(self,
                 rows: int,
                 cols: int,):
        self.rows = rows
        self.cols = cols
        self.data = []

        for row in range(rows):
            arr = []
            for col in range(cols):
                arr.append(0)
            self.data.append(arr)

    def map(self, func):
        self.data = [
            [func(col, r, c) for c, col in enumerate(row)] for r, row in enumerate(self.data)
        ]

    # @staticmethod
    # def static_map(A, func):
    #     matrix = Matrix(A.rows, A.cols)
    #
    #     matrix.data = [
    #         [func(col, r, c) for c, col in enumerate(row)] for r, row in enumerate(matrix.data)
    #     ]
    #     return matrix

    @staticmethod
    def array_to_matrix(arr: list):
        matrix = Matrix(len(arr), 1)

        def func(elm, i, j):
            return arr[i]

        matrix.map(func)
        return matrix

    def randomize(self):
        def func(elm, index_1, index_2):
            return random() * 2 - 1

        self.map(func)

    @staticmethod
    def add(A, B):
        matrix = Matrix(A.rows, A.cols)

        def sum_arrays(elm, index_1, index_2):
            return A.data[index_1][index_2] + B.data[index_1][index_2]

        matrix.map(sum_arrays)

        return matrix

    @staticmethod
    def multiply(A, B):
        matrix = Matrix(A.rows, B.cols)

        def func(elm, i, j):
            sum_all_multiply = 0

            for k in range(A.cols):
                sum_all_multiply += A.data[i][k] * B.data[k][j]

            return sum_all_multiply

        matrix.map(func)

        return matrix

