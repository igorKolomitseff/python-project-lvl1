from random import randint

GAME_DESCRIPTION = 'Answer "yes" if given number is prime. ' \
                   'Otherwise answer "no".'


def is_prime(number):
    """Check whether the number is prime."""

    if number < 2:
        return False

    for i in range(2, round(number / 2 + 1)):
        if number % i == 0:
            return False

    return True


def get_question_answer():
    """Get a random number as a question and the correct answer."""
    begin_of_range = 1
    end_of_range = 100

    random_number = randint(begin_of_range, end_of_range)
    question = f'Question: {random_number}'

    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (question, correct_answer)
