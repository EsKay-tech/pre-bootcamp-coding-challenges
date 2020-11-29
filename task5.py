import math


def area_of_triangle(a, b, c):
    semi_perimeter = 0.5*(a + b + c)

    # Heron's formula:
    area = math.sqrt(semi_perimeter*(semi_perimeter - a)*(semi_perimeter - b)*(semi_perimeter - c))

    return area
