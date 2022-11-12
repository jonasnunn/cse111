
# no 1
def compute_data(a, b, c, d):
    return (a/b) * (a/(c**2 + d**2))

def test_data():
    # declare test data
    data = []
    data.append([5,4,3,2, 0.4807692307692308])
    data.append([9, 1, 4, 6, 1.5576923076923077])

    #run tests
    for test in data :
        print(compute_data(test[0], test[1], test[2], test[3]) == test[4])

test_data()


#no 2
from math import sqrt
import re

def quadratic_formula(a, b, c):
    return (-b + sqrt(b**2-4*a*c)) / (2 * a)

print(quadratic_formula(9, 1, 4))

#no 3
import math 

def compute_area(r):
    return math.pi * r * r

radius = float(input("Please enter a radius: "))

print(f'The area is: {compute_area(radius)}')
