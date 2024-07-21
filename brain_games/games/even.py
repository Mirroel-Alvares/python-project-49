from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    num = randint(1, 99)
    question_data = num
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return question_data, correct_answer
