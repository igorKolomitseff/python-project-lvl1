from random import randint


GAME_DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_question_answer():
    """Get a random number as a question and the correct answer."""
    begin_of_range = 1
    end_of_range = 100
    min_step = 1
    max_step = 10
    min_index_item = 0
    max_index_item = 9

    first_number = randint(begin_of_range, end_of_range)
    random_step = randint(min_step, max_step)
    progression = [f'{first_number}']

    for i in range(1, PROGRESSION_LENGTH):
        progression.append(str(int(progression[i - 1]) + random_step))
    
    index_miss_number = randint(min_index_item, max_index_item)
    miss_number = progression[index_miss_number]
    progression[index_miss_number] = '..'

    progression = ' '.join(progression)

    question = f'Question: {progression}'
    correct_answer = miss_number

    return (question, correct_answer)
