
import secrets
import string


def generate_password(length=16):

    if length < 12 or length > 64:
        raise ValueError("Password length must be between 12 and 64.")

    uppercase = secrets.choice(string.ascii_uppercase)
    lowercase = secrets.choice(string.ascii_lowercase)
    number = secrets.choice(string.digits)
    symbol = secrets.choice("!@#$%^&*()-_+=")

    all_characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*()-_+="
    )

    remaining = [
        secrets.choice(all_characters)
        for _ in range(length - 4)
    ]

    password_list = [
        uppercase,
        lowercase,
        number,
        symbol
    ] + remaining

    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)
