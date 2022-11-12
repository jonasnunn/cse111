from math import sqrt

def quadratic_formula(a, b, c):
    return (-b + sqrt(b**2-4*a*c)) / (2 * a)

print(quadratic_formula(9, 1, 4))


