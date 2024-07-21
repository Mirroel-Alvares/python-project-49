from random import randint


GAME_TASK = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 20)
    step = randint(1, 4)
    random_progression = list(range(start, start + step * 8, step))
    return random_progression


def get_question_and_answer():
    progression = generate_progression()
    random_position = randint(0, len(progression) - 1)
    correct_answer = progression.pop(random_position)
    progression.insert(random_position, '..')
    question_data = " ". join([str(i) for i in progression])
    return question_data, correct_answer
