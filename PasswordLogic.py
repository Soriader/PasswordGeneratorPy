import secrets
import string


def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    character_set = ''

    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character set must be selected.")

    password = ''.join(secrets.choice(character_set) for _ in range(length))

    return password


def check_strength(password):
    length = len(password)
    strength = "Very Weak"

    if length >= 8:
        strength = "Weak"
    if length >= 12:
        strength = "Medium"
    if length >= 13:
        strength = "Strong"

    return strength