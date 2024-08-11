import random
import string

def generate_password(length):
    # Define a string containing all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random choices from `characters`
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage: Generate a password of length 12
password = generate_password(12)
print("Generated Password:", password)

