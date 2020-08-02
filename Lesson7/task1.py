class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        str = ''
        for el in self.data:
            str += f'{el}\n'
        return str

    def add_str(self, x, data_str):
        if (x <= len(data_str)):
            return data_str
        str = []
        for el in range(0, len(data_str[0])):
            str.append(0)
        for el in range(len(data_str), x):
            data_str.append(str)
        return data_str

    def add_colum(self, y, data_plus):
        current_y = len(data_plus[0])
        if (y <= current_y):
            return data_plus
        for j in range(0, len(data_plus)):
            for i in range(current_y, y):
                data_plus[j].append(0)
        return data_plus

    def __add__(self, other):

        data_new1 = self.data
        data_new2 = other.data

        if len(self.data) > len(other.data):
            data_new2 = other.add_str(len(self.data), other.data)
        else:
            data_new1 = self.add_str(len(other.data), self.data)
        if len(self.data[0]) > len(other.data[0]):
            data_new2 = other.add_colum(len(self.data[0]), other.data)
        else:
            data_new1 = self.add_colum(len(other.data[0]), self.data)

        for i in range(len(data_new2)):
            for j in range(len(data_new2[0])):
                data_new2[i][j] += data_new1[i][j]
        return Matrix(data_new2)


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

m_1 = Matrix(m1)
m_2 = Matrix(m2)
print(m_1)
print(m_2)
print(m_2 + m_1)
