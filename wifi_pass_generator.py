import random
import string
import argparse

def generate_wifi_password(length=12):
    # Define the character sets
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits              # 0-9
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"  # Special characters

    # Combine all characters
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

def arguments_validations(args: argparse.Namespace):
    pass

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Generate random Wi-Fi passwords.')
    parser.add_argument('num_passwords', type=int, help='Number of passwords to generate')
    parser.add_argument('--length', type=int, default=12, help='Length of each password (default: 12)')

    args = parser.parse_args()

    arguments_validations(args)

     # Open the output file
    with open('./wifi_passwords.txt', 'w') as file:
        # Generate the specified number of passwords
        for _ in range(args.num_passwords):
            wifi_password = generate_wifi_password(args.length)
            file.write(f"{wifi_password}\n")  # Write each password to the file

    print(f"Generated {args.num_passwords} Wi-Fi passwords and saved to ./wifi_passwords.txt")


if __name__ == "__main__":
    main()