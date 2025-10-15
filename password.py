import string
import random

# Character sets
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation

# Check password strength
def check_password_strength(password):
    length_ok = len(password) >= 8
    has_lower = any(char in LOWERCASE for char in password)
    has_upper = any(char in UPPERCASE for char in password)
    has_digit = any(char in DIGITS for char in password)
    has_symbol = any(char in SYMBOLS for char in password)

    return all([length_ok, has_lower, has_upper, has_digit, has_symbol])

# Improve weak password
def improve_password(password):
    improved = list(password)

    # Ensure minimum length
    while len(improved) < 8:
        improved.append(random.choice(DIGITS + SYMBOLS))

    # Add missing character types
    if not any(char in LOWERCASE for char in improved):
        improved.append(random.choice(LOWERCASE))
    if not any(char in UPPERCASE for char in improved):
        improved.append(random.choice(UPPERCASE))
    if not any(char in DIGITS for char in improved):
        improved.append(random.choice(DIGITS))
    if not any(char in SYMBOLS for char in improved):
        improved.append(random.choice(SYMBOLS))

    random.shuffle(improved)
    return ''.join(improved)

# Generate a strong password
def generate_password(length=12):
    if length < 8:
        length = 8

    password = [
        random.choice(LOWERCASE),
        random.choice(UPPERCASE),
        random.choice(DIGITS),
        random.choice(SYMBOLS)
    ]

    all_chars = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

# Main program
def main():
    answer = input("Do you already have a password? (yes/no): ").strip().lower()

    if answer == "yes":
        user_password = input("Enter your password: ")
        if check_password_strength(user_password):
            print("✅ Your password is strong.")
        else:
            print("❌ Your password is weak. Here's a stronger version based on it:")
            improved = improve_password(user_password)
            print("🔐 Improved password:", improved)
    elif answer == "no":
        new_password = generate_password()
        print("🔐 Suggested strong password:", new_password)
    else:
        print("Please enter only 'yes' or 'no'.")

# Run the program
main()