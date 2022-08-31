import prompt


NUMBERS_OF_ROUNDS = 3


def launch_game(game):
    """Run a game."""

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(game.GAME_DESCRIPTION)

    count_correct_answers = 0

    while count_correct_answers < NUMBERS_OF_ROUNDS:
        question, correct_answer = game.get_question_answer()

        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            count_correct_answers += 1

            print(('Correct!'))

        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return  # exit from the body of the loop and from the function

    print(f'Congratulations, {user_name}!')
