from random import randint


def choose_random_number():
    """Return an integer number from a range of numbers."""
    begin_of_range = 1
    end_of_range = 100

    random_number = randint(begin_of_range, end_of_range)

    return random_number
