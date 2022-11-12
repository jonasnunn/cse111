import math
from datetime import datetime


w = int(input('What is the width of the tire in mm? '))
a = int(input('What is the aspect ratio of the tire? '))
d = int(input('What is the diameater of the wheel? '))


v = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000
print(f'The volume is {v:.2f} liters')


day = datetime.today().date()

v = round(v, 2)
text = str(day) + ', ' + str(w) + ', ' + str(a) + ', ' + str(d) + ', ' + str(v) + '\n'

file = open('volume.txt', mode = 'at')
file.write(text)
file.close()