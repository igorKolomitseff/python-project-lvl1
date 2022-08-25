import prompt


def show_greeting():
    """The function prints a welcome message."""

    print('Welcome to the Brain Games!')


def ask_user_name():
    """The function asks for the user's name and returns it."""

    name = prompt.string('May I have your name? ')

    return name


def welcome_user(name):
    """The function greets the user."""

    print(f'Hello, {name}!')
