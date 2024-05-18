#!/usr/bin/env python3

import random
from brain_games.engine import run_game


GAME_RULE = 'What is the result of the expression?'


def calculate(operand1, operand2, operator):
    match operator:
        case '+':
            return operand1 + operand2
        case '-':
            return operand1 - operand2
        case '*':
            return operand1 * operand2
        case _:
            return None


def generate_calc_game():
    operators = ['+', '-', '*']
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operator = operators[random.randint(0, len(operators) - 1)]
    question = f'{operand1} {operator} {operand2}'
    answer = calculate(operand1, operand2, operator)

    return (question, str(answer))


def main():
    run_game(GAME_RULE, generate_calc_game)


if __name__ == '__main__':
    main()
