#!/usr/bin/env python3

from random import randint


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for i in range(2, num // 2):
            if (num % i) == 0:
                return False
        return True


def game():
    num = randint(1, 99)
    question = (f'Question: {num}')
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
