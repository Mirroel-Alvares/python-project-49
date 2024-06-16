#!/usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.game_modules import gcd


def main():
    run_game(gcd)


if __name__ == '__main__':
    main()