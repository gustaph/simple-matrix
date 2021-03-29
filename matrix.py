class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix = [[int(index) for index in row.split(' ')] for row in self.matrix_string.split('\n')]

    def show_matrix(self):
        for row in self.matrix:
            print(row)

    # index starts with 1
    def row(self, index):
        return self.matrix[:][index-1]

    # index starts with 1
    def column(self, index):
        return [element[index-1] for element in self.matrix]

if __name__ == '__main__':
    # tests
    matrix = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
    matrix.show_matrix()
    print(matrix.column(4)) # [4, 8, 6]
    print(matrix.row(2)) # [5, 6, 7, 8]