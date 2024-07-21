from random import randint


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def get_greater_common_divisor(num1, num2):
    divisors = []
    for i in range(1, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    return max(divisors)


def get_question_and_answer():
    num_one = randint(1, 100)
    num_two = randint(1, 100)
    question_data = f'{num_one} {num_two}'
    correct_answer = get_greater_common_divisor(num_one, num_two)
    return question_data, correct_answer
