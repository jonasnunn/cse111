# print(round(len(str(float(int(input('Enter something?')))))))

# one = 1
# print(f'Hello, I, ',sep='  ',end='\n', file='test.py', flush=True)


# def my_fun():
#     import math 
#     x = math.ceil(17 ** 9 / 3) - 6 


#     if x % 2 ==  0:
#         t_or_f = True
#     else:
#         t_or_f = False

#     return t_or_f

# print(my_fun())

# import random 
# l = []

# for i in range(5):
#     l.append(random.randrange(1,1000))

# l.sort()
# print(l)
from datetime import datetime

now = datetime.now()
display_message = 'even_minute'
if (now.minute % 2 > 0):
    display_message = 'odd_minute'
print(display_message)