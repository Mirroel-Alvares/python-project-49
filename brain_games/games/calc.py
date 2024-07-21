from random import randint
from operator import add, mul, sub


GAME_TASK = 'What is the result of the expression?'


def get_question_and_answer():
    first_num = randint(20, 40)
    second_num = randint(1, 20)
    operations = [
        ('*', mul),
        ('+', add),
        ('-', sub)
    ]
    random_operation = operations[randint(0, len(operations) - 1)]
    question_data = f'{first_num} {random_operation[0]} {second_num}'
    correct_answer = random_operation[1](first_num, second_num)
    return question_data, correct_answer
