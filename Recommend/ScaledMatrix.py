"""ScaledMatrix"""


def scale(row, col):
    """Function"""
    matrix = []
    for _ in range(row):
        value_l = []
        for _ in range(col):
            value = float(input())
            value_l.append(value)
        matrix.append(value_l)
    scale_matrix = matrix - min(matrix) / max(matrix) - min(matrix)
    for i in scale_matrix:
        print()
        for j in i:
            print("%.2f" % j, end=" ")


scale(int(input()), int(input()))
