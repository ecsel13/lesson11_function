def get_matrix(n, m, value):
    matrix = []
    if n * m * value == 0:
        print(matrix)
    else:
        for i in range(1, n + 1):
            matrix1 = []
            matrix.append(matrix1)
            for j in range(1, m + 1):
                matrix1.append(value)
        print(matrix)


get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
