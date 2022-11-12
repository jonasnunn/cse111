

# width = float(input('What is the width of the rectangle: '))
# length = float(input('What is the heigth of the rectangle: '))

def area_rectangle(w = float(input('What is the width of the rectangle: ')),l = float(input('What is the length of the rectangle: '))):
    area = w * l
    return area


n = int(input('How many rectangles are there? '))



print(f'{area_rectangle():.2f}')