#!/usr/bin/env python3

from random import randint


GAME_TASK = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 20)
    step = randint(1, 4)
    random_progression = []
    while len(random_progression) < 8:
        random_progression.append(start)
        start += step
    return random_progression


def game():
    progression = generate_progression()
    random_position = randint(0, len(progression) - 1)
    correct_answer = progression.pop(random_position)
    progression.insert(random_position, '..')
    question = " ". join([str(i) for i in progression])
    return question, correct_answer
