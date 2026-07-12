import random
import string


def generate_password(length, include_digits=True, include_special=True):
    # Core character sets
    letters = string.ascii_letters  # Contains both lowercase and uppercase
    digits = string.digits if include_digits else ""
    special_chars = string.punctuation if include_special else ""

    # Combine the allowed characters
    all_characters = letters + digits + special_chars

    if not all_characters:
        return "Error: No characters selected for the password."

    # Generate a random password of the specified length
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    print("PASSWORD GENERATOR")

    # 1. User Input: Prompt for password length
    while True:
        try:
            length = int(
                input("Enter the desired length of the password (min 4): ")
            )
            if length < 4:
                print("Please enter a length of at least 4 for security.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Optional Complexity Inputs
    include_digits = (
        input("Include numbers? (y/n): ").strip().lower() == "y"
    )
    include_special = (
        input("Include special characters? (y/n): ").strip().lower() == "y"
    )

    # 2. Generate Password
    generated_password = generate_password(
        length, include_digits, include_special
    )

    # 3. Display the Password
    print("\n" + "=" * 35)
    print(f"Generated Password: {generated_password}")
    print("=" * 35)


if __name__ == "__main__":
    main()
