#!/usr/bin/env python3
from random import randint
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


def is_even(number):
    """Check whether the number is even."""
    divider = 2

    return number % divider == 0


def show_rules_game():
    """Show the rules of the game."""

    print('Answer "yes" if the number is even, otherwise answer "no".')


def ask_and_answer():
    """Select a random number, print the question and ask
    the user for the answer. Return the random number and the
    answer."""
    random_number = choose_random_number()

    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ').lower()

    return (random_number, answer)


def show_correct_answer(answer, correct_answer, user_name):
    """Print the correct answer."""

    print(f"'{answer}' is wrong answer ;(.", end=" ")
    print(f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {user_name}!")


def is_even_game(user_name):
    """Ask the user if the number is even."""
    count_correct_answers = 0  # counter of correct answers

    random_number, answer = ask_and_answer()

    while count_correct_answers < 3:

        if ((answer == 'yes' and is_even(random_number))
                or (answer == 'no' and not is_even(random_number))):
            count_correct_answers += 1

            print('Correct!')

            if count_correct_answers == 3:
                print(f'Congratulations, {user_name}!')
                break

            random_number, answer = ask_and_answer()

        elif answer != 'yes' and is_even(random_number):
            correct_answer = 'yes'

            show_correct_answer(answer, correct_answer, user_name)
            break

        elif answer != 'no' and not is_even(random_number):
            correct_answer = 'no'

            show_correct_answer(answer, correct_answer, user_name)
            break


def main():
    show_greeting()
    user_name = ask_user_name()
    welcome_user(user_name)
    show_rules_game()
    is_even_game(user_name)


if __name__ == '__main__':
    main()
