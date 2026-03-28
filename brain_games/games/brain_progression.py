import random


GAME_RULE = 'What number is missing in the progression?'


def generate_progression(first, diff, length):
    return [first + n * diff for n in range(length)]


def build_question(progression, hidden_index):
    parts = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            parts.append('..')
        else:
            parts.append(str(num))
    return ' '.join(parts)


def generate_game():
    first = random.randint(-15, 15)
    diff = random.randint(1, 15)
    progression_length = random.randint(5, 15)
    hidden_index = random.randint(0, progression_length - 1)

    progression = generate_progression(first, diff, progression_length)
    answer = str(progression[hidden_index])
    question = build_question(progression, hidden_index)

    return (question, answer)
