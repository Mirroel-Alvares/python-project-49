from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    num = randint(1, 99)
    question = (f'Question: {num}')
    if num % 2 == 0:
        correct_answer = 'yes'
    elif num % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer
