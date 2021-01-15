def get_e(n: int) -> float:
    return (1 + 1 / n) ** n


def get_e_iterating():
    euler = 2.71
    e = 0
    i = 1

    while e < euler:
        e = get_e(i)
        i += 1

    return e, i


euler_number, number_of_iterations = get_e_iterating()

print(number_of_iterations, euler_number)
