import numpy as np


def multiples(x):
    num_list = np.arange(1, x)
    emp_list = []

    for i in num_list:
        if i % 3 == 0 or i % 5 == 0:
            emp_list.append(i)
        else:
            continue

    total = sum(emp_list)
    return total


print("Sum of multiples is", multiples(1000))
