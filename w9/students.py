import csv

def main():
    dictionary = read_dict('students.csv', 0)
    i_number = input("Plase enter an i number: ")
    i_number = i_number.replace("-","")
    if len(i_number) > 9:
        print("Too many digits")
        return 
    elif len(i_number) < 9:
        print("Too few digits")
        return 

    valid_i_number = False
    for keys in dictionary:
        if i_number == keys:
            valid_i_number = True
    if valid_i_number:
        name = dictionary[i_number][1]
        print(name)
    else:
        print("No such student")

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            compound_dict[key] = row_list
    return compound_dict


if __name__ == "__main__":
    main()

