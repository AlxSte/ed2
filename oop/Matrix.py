class Matrix:

    def __init__(self, el_list):
        self.el_list = el_list

    def __str__(self):
        for el in self.el_list:
            return "\n".join(map(str, self.el_list))

    def __add__(self, other):
        result = []
        for i in range(len(self.el_list)):
            result.append([])
            for j in range(len(self.el_list[0])):
                result[i].append(self.el_list[i][j] + other.el_list[i][j])
        return Matrix(result)


el_ls = [[1, 2, 3, 4],
         [3, 4, 5, 6]]

el_ls2 = [[2, 3, 4, 5],
          [6, 7, 8, 9]]

matrix = Matrix(el_ls)
matrix2 = Matrix(el_ls2)
print(matrix + matrix2)

git





