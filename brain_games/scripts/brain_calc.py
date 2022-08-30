from random import randint
from random import choice
import prompt
from brain_games.scripts.greeting import show_greeting
from brain_games.scripts.greeting import ask_user_name
from brain_games.scripts.greeting import welcome_user


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
    answer = int(prompt.string('Your answer: '))

    return (first_operand, second_operand, math_operator, answer)


def calc_correct_answer(first_operand, second_operand, math_operator):
    """Return the correct answer."""

    if math_operator == '+':
        return first_operand + second_operand
    elif math_operator == '-':
        return first_operand - second_operand
    elif math_operator == '*':
        return first_operand * second_operand


def show_correct_answer(answer, correct_answer, user_name):
    """Print the correct answer."""

    print(f"'{answer}' is wrong answer ;(.", end=" ")
    print(f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {user_name}!")


def calc_game(user_name):
    """Show a random mathematical expression to be calculated and
    ask the user to write down the correct answer."""
    count_correct_answers = 0  # counter of correct answers

    first_operand, second_operand, math_operator, answer = ask_and_answer()
    correct_answer = calc_correct_answer(first_operand, second_operand, math_operator)

    while count_correct_answers < 3:

        if answer == correct_answer:
            count_correct_answers += 1

            print('Correct!')

            if count_correct_answers == 3:
                print(f'Congratulations, {user_name}!')
                break

            first_operand, second_operand, math_operator, answer = ask_and_answer()
            correct_answer = calc_correct_answer(first_operand, second_operand, math_operator)

        elif answer != correct_answer:

            show_correct_answer(answer, correct_answer, user_name)
            break


def main():
    show_greeting()
    user_name = ask_user_name()
    welcome_user(user_name)
    show_rules_game()
    calc_game(user_name)


if __name__ == '__main__':
    main()
