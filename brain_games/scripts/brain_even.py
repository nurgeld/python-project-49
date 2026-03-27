#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.brain_even import generate_game, GAME_RULE


def main():
    run_game(GAME_RULE, generate_game)


if __name__ == '__main__':
    main()
