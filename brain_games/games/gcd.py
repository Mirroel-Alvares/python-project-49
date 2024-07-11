from random import randint


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def integer_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def get_question_and_answer():
    num_one = randint(1, 100)
    num_two = randint(1, 100)
    question = (f'Question: {num_one} {num_two}')
    correct_answer = max(
        set(integer_divisors(num_one)) & set(integer_divisors(num_two))
    )
    return question, correct_answer
