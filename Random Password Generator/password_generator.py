import random
import string


# Function to generate password
def generate_password(length):
    # Characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# Main program
print("=== Password Generator ===")
length = int(input("Enter password length: "))

password = generate_password(length)

print("Generated Password:", password)