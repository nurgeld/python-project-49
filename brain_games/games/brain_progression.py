import random
from brain_games.engine import run_game


GAME_RULE = 'What number is missing in the progression?'


def calculate_element_of_progression(first, difference, index):
    return first + index * difference


def generate_progression(first, difference, progression_length):
    progression = []
    for n in range(progression_length):
        nth_term = first + n * difference
        progression.append(nth_term)
    return progression


def mask_element(coll, index):
    result = coll[:]
    result[index] = '..'
    return result


def generate_progression_game():
    first = random.randint(-15, 15)
    difference = random.randint(1, 15)
    progression_length = random.randint(5, 15)
    index_of_masked_element = random.randint(0, progression_length - 1)
    progression = generate_progression(first, difference, progression_length)
    masked_progression = mask_element(progression, index_of_masked_element)
    question = ' '.join(str(x) for x in masked_progression)
    answer = calculate_element_of_progression(first, difference, index_of_masked_element)

    return (question, str(answer))


if __name__ == '__main__':
    run_game(GAME_RULE, generate_progression_game)
