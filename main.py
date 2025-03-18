import string
import secrets

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None
    
    # Define character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure password contains at least one of each type
    password = [
        secrets.choice(upper),
        secrets.choice(lower),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Fill the rest of the password with random choices
    all_chars = upper + lower + digits + special
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

# Get user input
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print("\n🔐 Your Generated Password: ", password)
except ValueError:
    print("Please enter a valid number.")
