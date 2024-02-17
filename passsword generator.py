#importing string and random module
import string
import random

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation+string.whitespace

    # Ensure at least one uppercase letter, one lowercase letter, one digit, and one special character
    password = [random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits),
                random.choice(string.punctuation),
                random.choice(string.whitespace)]

    # Fill the remaining length with random choices from the characters
    for _ in range(length - 4):
        password.append(random.choice(characters))

   # Shuffling the string values in the password list
    random.shuffle(password)

    # Concatenation of values into single string
    # without any separation
    password = ''.join(password)

    return password

def main():
    option = input("Do you want to generate a strong password (Yes/No)? ").lower()

    if option == "yes":
        password_length = int(input("Enter the length of the password: "))
        if password_length < 8:
            print("Password length must be at least 8 characters.")
            return

        password = generate_strong_password(password_length)
        print("Generated strong password:", password)

    elif option == "no":
       print("Program terminated. Thank you!")
    else:
        print("Invalid input!!! Please enter Yes/No")
main()
