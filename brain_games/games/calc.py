from random import randint, choice

GAME_DESCRIPTION = 'What is the result of the expression?'
MATH_OPERATORS = ('+', '-', '*')


def get_question_answer():
    """Get a random number as a question and the correct answer."""
    begin_of_range = 1
    end_of_range = 100

    first_operand = randint(begin_of_range, end_of_range)
    second_operand = randint(begin_of_range, end_of_range)
    math_operator = choice(MATH_OPERATORS)

    question = f'Question: {first_operand} {math_operator} {second_operand}'

    if math_operator == '+':
        correct_answer = str(first_operand + second_operand)
    elif math_operator == '-':
        correct_answer = str(first_operand - second_operand)
    elif math_operator == '*':
        correct_answer = str(first_operand * second_operand)

    return (question, correct_answer)
