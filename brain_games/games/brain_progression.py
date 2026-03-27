import random


GAME_RULE = 'What number is missing in the progression?'


def generate_game():
    first = random.randint(-15, 15)
    diff = random.randint(1, 15)
    progression_length = random.randint(5, 15)
    index_of_masked_element = random.randint(0, progression_length - 1)

    progression = [
        first + n * diff for n in range(progression_length)
    ]
    progression[index_of_masked_element] = '..'
    question = ' '.join(str(x) for x in progression)
    answer = str(first + index_of_masked_element * diff)

    return (question, answer)
