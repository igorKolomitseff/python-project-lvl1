from random import randint
from math import gcd


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    """Get a random number as a question and the correct answer."""
    begin_of_range = 1
    end_of_range = 100

    first_number = randint(begin_of_range, end_of_range)
    second_number = randint(begin_of_range, end_of_range)

    question = f'Question: {first_number} {second_number }'
    correct_answer = gcd(first_number, second_number)

    return (question, correct_answer)
