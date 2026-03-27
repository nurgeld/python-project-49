import random


GAME_RULE = 'Balance the given number'


def balance_number(number):
    digits = [int(d) for d in str(number)]
    total = sum(digits)
    length = len(digits)
    balanced_digits = [total // length] * length
    remainder = total % length

    for i in range(remainder):
        balanced_digits[i] += 1

    return ''.join(str(d) for d in balanced_digits)


def generate_balance_game():
    number = random.randint(1, 1000000)
    question = str(number)
    answer = balance_number(number)

    return (question, answer)
