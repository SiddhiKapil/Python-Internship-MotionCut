import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("Welcome to the Strong Password Generator!")
    
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                print("Please enter a valid positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            password_length = int(input("Enter the length of each password: "))
            if password_length <= 0:
                print("Please enter a valid positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    passwords = generate_multiple_passwords(num_passwords, password_length)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
