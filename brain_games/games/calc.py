from random import randint


GAME_TASK = 'What is the result of the expression?'


def get_question_and_answer():
    first_num = randint(20, 40)
    second_num = randint(1, 20)
    expressions = (
        first_num * second_num,
        first_num + second_num,
        first_num - second_num
    )
    str_expressions = (
        f'{first_num} * {second_num}',
        f'{first_num} + {second_num}',
        f'{first_num} - {second_num}'
    )
    rand_expressions = randint(0, 2)
    question = (f'Question: {str_expressions[rand_expressions]}')
    correct_answer = expressions[rand_expressions]
    return question, correct_answer
