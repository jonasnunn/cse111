import math 
n_items = int(input('Enter the number of items: '))
n_per_b = int(input('Enter the number of items per box: '))
boxes = n_items/n_per_b
boxes_rounded_up = math.ceil(boxes)
print(f'For {n_items} items, packing {n_per_b} items in each box, you will need {boxes_rounded_up} boxes.')