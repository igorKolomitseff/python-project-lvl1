import prompt


def show_greeting():
    """Print a welcome message."""

    print('Welcome to the Brain Games!')


def ask_user_name():
    """Ask for the user's name and return it."""

    name = prompt.string('May I have your name? ')

    return name


def welcome_user(name):
    """Greet the user."""

    print(f'Hello, {name}!')
