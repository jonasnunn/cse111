import random


my_list = []

def add_to_end(number):
    my_list.append(number)


def add_to_somewhere(number):
    random_number = random.randint(0,len(my_list))
    my_list.insert(random_number, number)

def remove_item():
    my_list.pop()


for _ in range(5):
    add_to_end(5)
    add_to_somewhere(4)
    remove_item()

print(my_list)
