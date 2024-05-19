import random


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    if number2 == 0:
        return number1

    return get_gcd(number2, number1 % number2)


def generate_gcd_game():
    number1 = random.randint(1, 200)
    number2 = random.randint(1, 200)
    question = f'{number1} {number2}'
    answer = get_gcd(number1, number2)

    return (question, str(answer))


if __name__ == '__main__':
    generate_gcd_game()
