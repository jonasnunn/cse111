def main():
    score = get_answers()
    print(f'Your score is {score}')
    print('A score below 15 may indicate you suck')


def ans_to_num(letter):
    if letter == "D":
        value = 0
    elif letter == "d":
        value = 1
    elif letter == "a":
        value = 2
    elif letter == "A":
        value = 3
    return value

def neg_ans_to_num(letter):
    if letter == "D":
        value = 3
    elif letter == "d":
        value = 2
    elif letter == "a":
        value = 1
    elif letter == "A":
        value = 0
    return value
    

def get_answers():
    q1 = ans_to_num(input("I feel that I am a person of worth, at least on an equal plane with others.(D,d,a,A)"))
    q2 = ans_to_num(input("I feel that I have a number of good qualities.(D,d,a,A)"))
    q3 = neg_ans_to_num(input("All in all, I am inclined to feel that I am a failure.(D,d,a,A)"))
    q4 = ans_to_num(input("I am able to do things as well as most other people.(D,d,a,A)"))
    q5 = neg_ans_to_num(input("I feel I do not have much to be proud of.(D,d,a,A)"))
    q6 = ans_to_num(input("I take a positive attitude toward myself.(D,d,a,A)"))
    q7 = ans_to_num(input("On the whole, I am satisfied with myself.(D,d,a,A)"))
    q8 = neg_ans_to_num(input("I wish I could have more respect for myself.(D,d,a,A)"))
    q9 = neg_ans_to_num(input("I certainly feel useless at times.(D,d,a,A)"))
    q10 = neg_ans_to_num(input("At times I think I am no good at all.(D,d,a,A)"))

    total = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
    return total

main()