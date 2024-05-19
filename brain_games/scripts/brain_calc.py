#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.brain_calc import generate_calc_game, GAME_RULE


def main():
    run_game(GAME_RULE, generate_calc_game)


if __name__ == '__main__':
    main()
