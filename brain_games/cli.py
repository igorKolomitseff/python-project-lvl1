import prompt


def welcome_user():
    """The function asks for the user's name and welcomes him."""

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
