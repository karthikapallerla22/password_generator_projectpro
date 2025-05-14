import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character set must be selected")

    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(character_pool))

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    pwd = generate_password(length=16)
    print("Generated Password:", pwd)
