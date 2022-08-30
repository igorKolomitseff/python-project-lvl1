from random import randint
from random import choice
import prompt

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


def ask_and_answer():
    """Select random operands and a random operator, print the question 
    and ask the user for the answer. Return random operands, the random
    operator and the answer."""
    first_operand = choose_random_number()
    second_operand = choose_random_number()
    math_operator = choose_math_operator()

    print(f'Question: {first_operand} {math_operator} {second_operand}')
    answer = prompt.string('Your answer: ')

    return (first_operand, second_operand, math_operator, answer)


def calc_correct_answer(first_operand, second_operand, math_operator):
    """Return the correct answer."""

    if math_operator == '+':
        return first_operand + second_operand
    elif math_operator == '-':
        return first_operand - second_operand
    elif math_operator == '*':
        return first_operand * second_operand
