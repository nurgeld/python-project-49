#!/usr/bin/env python3

import random
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def is_even(num):
    return num % 2 == 0


def get_random_num(max):
    return random.randint(0, max)


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUM_FOR_QUESTION = 200
MAX_STEPS = 3


def run_brain_even_game():
    username = welcome_user()
    print(GAME_RULES)

    for i in range(MAX_STEPS):
        question = get_random_num(MAX_NUM_FOR_QUESTION)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(question) else 'no'
        error_message = (
            f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
        )

        if answer != correct_answer:
            print(error_message)
            print(f"Let's try again, {username}!")
            break
        else:
            print('Correct!')

        if i == MAX_STEPS - 1:
            print(f'Congratulations, {username}!')


def main():
    greet()
    run_brain_even_game()


if __name__ == '__main__':
    main()
