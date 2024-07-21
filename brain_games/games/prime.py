from random import randint


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_question_and_answer():
    num = randint(1, 99)
    question_data = num
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question_data, correct_answer
