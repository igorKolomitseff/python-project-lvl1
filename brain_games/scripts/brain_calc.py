from random import randint
from random import choice


def choose_random_number():
    """Return an integer number from a range of numbers."""
    begin_of_range = 1
    end_of_range = 100

    random_number = randint(begin_of_range, end_of_range)

    return random_number


def choose_math_operator():
    """Return random math operator: '+', '-' or '*'."""
    math_operators = ('+', '-', '*')

    random_math_operator = choice(math_operators)

    return random_math_operator


def show_rules_game():
    """Show the rules of the game."""

    print('What is the result of the expression?.')
