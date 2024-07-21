#!/usr/bin/env python3

from brain_games.cli import welcome_user
import prompt


def run_game(module):
    name = welcome_user()
    roundsCount = 3
    print(module.GAME_TASK)
    for round in range(roundsCount):
        question_data, correct_answer = module.get_question_and_answer()
        print(f'Question: {question_data}')
        answer = prompt.string('Your answer: ')
        if answer != str(correct_answer):
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                f"Let's try again, {name}!"
            )
            return
        print('Correct!')

    print(f'Congratulations, {name}!')
