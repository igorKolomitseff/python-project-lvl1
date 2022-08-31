from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Check whether the number is even."""
    divider = 2

    return number % divider == 0


def get_question_answer():
    """Get a random number as a question and the correct answer."""
    begin_of_range = 1
    end_of_range = 100

    random_number = randint(begin_of_range, end_of_range)
    question = f'Question: {random_number}'

    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (question, correct_answer)
