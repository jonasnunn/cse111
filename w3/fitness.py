# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Gender (m/f): ')
    birthday = input('What is your birthday(YYYY-MM-DD): ')
    height = float(input('What is your heigth(in): '))
    weigth = float(input('What is your weight(lbs): '))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthday)
    kilos = kg_from_lb(weigth)
    cms = cm_from_in(height)
    body_mass = body_mass_index(kilos, cms)
    bmrs = basal_metabolic_rate(gender, kilos, cms, age)
    # Print the results for the user to see.
    print(f'Age: {age}')
    print(f'Weigth (kg): {kilos:.2f}')
    print(f'Heigth (cm): {cms:.2f}')
    print(f'BMI: {body_mass:.2f}')
    print(f'BMR: {bmrs:.2f}')
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = pounds * .45359237 
    return kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = 2.54 * inches
    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / height**2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == 'f':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.33 * age
    elif gender == 'm':
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else:
        print('Please select m or f for gender')
    return bmr


# Call the main function so that
# this program will start executing.
main()