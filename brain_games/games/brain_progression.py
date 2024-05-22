import random


GAME_RULE = 'What number is missing in the progression?'


def take_element_of_progression(first, difference, index):
    return first + index * difference


def generate_progression(first, diff, progression_length):
    progression = []
    for n in range(progression_length):
        nth_term = first + n * diff
        progression.append(nth_term)
    return progression


def mask_element(coll, index):
    result = coll[:]
    result[index] = '..'
    return result


def generate_progression_game():
    first = random.randint(-15, 15)
    diff = random.randint(1, 15)
    progression_length = random.randint(5, 15)
    index_of_masked_element = random.randint(0, progression_length - 1)
    progression = generate_progression(first, diff, progression_length)
    masked_progression = mask_element(progression, index_of_masked_element)
    question = ' '.join(str(x) for x in masked_progression)
    answer = take_element_of_progression(first, diff, index_of_masked_element)

    return (question, str(answer))
