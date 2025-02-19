import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length you want for the password: "))
    password = generate_password(password_length)
    print("Generated random password:", password)

if __name__ == "__main__":
    main()