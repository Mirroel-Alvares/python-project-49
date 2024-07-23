from random import randint, randrange


GAME_TASK = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 20)
    step = randint(1, 4)
    stop = start + step * randint(6, 9)
    random_progression = list(range(start, stop, step))
    return random_progression


def get_question_and_answer():
    progression = generate_progression()
    random_position = randrange(len(progression))
    correct_answer = progression[random_position]
    progression[random_position] = '..'
    question_data = " ".join(map(str, progression))
    return question_data, correct_answer
