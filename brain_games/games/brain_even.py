import random


def is_even(num):
    return num % 2 == 0


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_even_game():
    question = random.randint(1, 200)
    answer = 'yes' if is_even(question) else 'no'
    return (question, answer)
