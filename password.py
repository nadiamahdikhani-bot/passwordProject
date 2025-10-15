Charaimport string
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

    if all([length_ok, has_lower, has_upper, has_digit, has_symbol]):
        return "✅ Your password is strong."
    else:
        return "❌ Your password is weak. It should include uppercase, lowercase, digits, symbols, and be at least 8 characters long."

# Generate a strong password
def generate_password(length=12):
    if length < 8:
        length = 8  # Minimum length

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

# Simple user interface
def main():
    answer = input("Do you already have a password? (yes/no): ").strip().lower()

    if answer == "yes":
        user_password = input("Enter your password: ")
        result = check_password_strength(user_password)
        print(result)
    elif answer == "no":
        new_password = generate_password()
        print("🔐 Suggested strong password:", new_password)
    else:
        print("Please enter only 'yes' or 'no'.")

# Run the program
main()