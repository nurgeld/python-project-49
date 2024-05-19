import prompt
from brain_games.cli import welcome_user, greet


MAX_STEPS = 3


def run_game(game_rule, game_parts):
    greet()
    username = welcome_user()
    print(game_rule)

    for i in range(MAX_STEPS):
        question, correct_answer = game_parts()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;( "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {username}!")
            return
        print('Correct!')

    print(f'Congratulations, {username}!')
