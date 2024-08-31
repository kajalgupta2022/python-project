import random
import string

def generate_password(length=12):
    """Generate a random password of a given length."""
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Define the possible characters for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one of each required character type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)

    # Join the list into a string to form the final password
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")

if __name__ == "__main__":
    main()
