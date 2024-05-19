import random


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number, curr_number=2):
    if number <= 1:
        return False
    if curr_number ** 2 > number:
        return True
    if number % curr_number == 0:
        return False
    return is_prime(number, curr_number + 1)


def generate_prime_game():
    question = random.randint(1, 200)
    answer = 'yes' if is_prime(question) else 'no'

    return (question, answer)


if __name__ == '__main__':
    generate_prime_game()
