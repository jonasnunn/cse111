def main():
    people_list = []
    num_members = int(input("How many family members do you have: "))
    for _ in range(num_members):
        person_dict = get_name_and_age()    
        people_list.append(person_dict)

    my_file = open("text.txt", "w")
    my_file.write(str(people_list))
    my_file.close()


def get_name_and_age():
    name = input("What is your family members name: ")
    age = input("What is their age: ")
    person_dict = {'name': name, 'age': age}
    return person_dict

main()