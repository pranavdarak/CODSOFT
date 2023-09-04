import random
import string

def password_generator(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password
#Adding execption Handling
try:
    password_len = int(input("Enter the desired password length : "))
    if password_len <= 0:
        print("Password length must be a positive integer.")
    else:
        # Generate and display the password
        generated_password = password_generator(password_len)
        print("Generated Password:", generated_password)
except ValueError:
    print("Invalid input.")
