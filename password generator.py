import random
import string

def generate_password(length):
    # Define the character set to use for password generation
    characters = string.ascii_letters + string.digits
    
    # Generate a random password from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        # Ensure the length is positive
        if length <= 0:
            print("Password length must be a positive integer.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
