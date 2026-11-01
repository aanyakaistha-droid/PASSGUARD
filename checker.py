
import re
import string


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou",
    "abc123",
    "111111",
    "000000",
    "password1"
}

KEYBOARD_PATTERNS = [
    "qwerty",
    "asdfgh",
    "zxcvbn",
    "qwert",
    "asdf",
    "12345",
    "54321",
    "09876"
]


def has_sequence(password):

    password = password.lower()

    sequences = [
        string.ascii_lowercase,
        string.digits
    ]

    for sequence in sequences:

        for i in range(len(sequence) - 3):

            pattern = sequence[i:i + 4]

            reverse_pattern = pattern[::-1]

            if pattern in password or reverse_pattern in password:
                return True

    return False


def check_password(password):

    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    # Check special characters
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    # Common password detection
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append(
            "This is a commonly used password. Choose something unique."
        )

    # Repeated character detection
    if re.search(r"(.)\1\1", password):
        score = max(0, score - 1)
        feedback.append(
            "Avoid repeating the same character three or more times."
        )

    # Keyboard pattern detection
    if any(pattern in password.lower() for pattern in KEYBOARD_PATTERNS):
        score = max(0, score - 1)
        feedback.append(
            "Avoid predictable keyboard patterns."
        )

    # Number and alphabet sequence detection
    if has_sequence(password):
        score = max(0, score - 1)
        feedback.append(
            "Avoid predictable sequences such as ABCD or 1234."
        )

    # Determine final strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


if __name__ == "__main__":

    password = input("Enter a test password: ")

    strength, feedback = check_password(password)

    print("Password strength:", strength)

    for suggestion in feedback:
        print("-", suggestion)
