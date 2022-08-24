from random import randint
import prompt


def choose_random_number():
    """The function returns an integer number from a range
    of numbers."""
    begin_of_range = 1
    end_of_range = 100

    random_number = randint(begin_of_range, end_of_range)

    return random_number


def is_even(number):
    """The function checks whether the number is even."""
    divider = 2

    return number % divider == 0


def show_rules_game():
    """The function shows the rules of the game."""

    print('Answer "yes" if the number is even, otherwise answer "no".')



def ask_and_answer():
    """The function selects a random number, prints the question and asks
    the user for the answer. Returns the random number and the
    answer."""
    random_number = choose_random_number()

    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ').lower()

    return (random_number, answer)
