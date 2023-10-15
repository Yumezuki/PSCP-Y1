"""Niwarn World"""


def function_x(var_n):
    """x"""
    import math

    total = 2 + ((math.log2(var_n**2)) / ((2 * var_n) * (math.log2(var_n))))
    return total


def function_y(var_n, var_s):
    """x"""
    import math

    total = (math.sin(math.radians(30)) + math.sqrt(2 * var_s)) / (
        (function_x(var_n)) + 3
    )
    return total


def function_z(var_k):
    """x"""
    total = (function_y(var_k, var_k) ** 2) + (
        (8456 * (function_x(var_k) ** 4)) / (24 * var_k)
    )
    return total


def niwarn(var_n, var_s, var_k):
    """Function"""
    total_x, total_y, total_z = (
        function_x(var_n),
        function_y(var_n, var_s),
        function_z(var_k),
    )
    print("X: %.1f, Y: %.1f, Z: %.1f" % (total_x, total_y, total_z))


niwarn(float(input()), float(input()), float(input()))
