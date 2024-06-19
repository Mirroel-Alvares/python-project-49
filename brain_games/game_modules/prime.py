#!/usr/bin/env python3

from random import randint


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
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
