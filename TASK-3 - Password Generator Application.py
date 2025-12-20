# CodSoft Python Internship Task
# Task Name: Password Generator
# Author: Kaavya B M

import random
import string

def get_password_length():
    """Get valid password length from user"""
    try:
        length = int(input("Enter desired password length (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters.")
            return None
        return length
    except ValueError:
        print("Please enter a valid number.")
        return None

def generate_password(length):
    """Generate a strong random password"""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+"

    # Ensure password has all character types
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols

    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)
    return "".join(password_chars)

# Main Program
print("\n--- PASSWORD GENERATOR ---")

length = get_password_length()

if length:
    password = generate_password(length)
    print("\nGenerated Password:")
    print(password)
