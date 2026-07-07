import random


def get_computer_choice():
    """Generates a random choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """Determines the winner based on game logic.

    Returns: 'tie', 'user', or 'computer'
    """
    if user_choice == computer_choice:
        return "tie"

    # Winning conditions for the user
    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"

    return "computer"


def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    round_number = 1

    print("=======================================")
    print("  Welcome to Rock, Paper, Scissors!   ")
    print("=======================================")
    print("Rules: Rock beats Scissors | Scissors beat Paper | Paper beats Rock\n")

    while True:
        print(f"--- Round {round_number} ---")

        # 1. User Input with validation
        user_choice = ""
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = (
                input("Enter your choice (rock, paper, scissors): ")
                .strip()
                .lower()
            )
            if user_choice not in ["rock", "paper", "scissors"]:
                print("Invalid input. Please try again.")

        # 2. Computer Selection
        computer_choice = get_computer_choice()

        # 3. Display Choices
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        # 4. Game Logic & Display Result
        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("👉 It's a tie!")
        elif result == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 Computer wins this round!")
            computer_score += 1

        # 5. Score Tracking
        print(f"\n[Current Score] You: {user_score} | Computer: {computer_score}")
        print("-" * 30)

        # 6. Play Again
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\n=======================================")
            print("             GAME OVER                ")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🏆 Congratulations! You won the game!")
            elif user_score < computer_score:
                print("🤖 Computer wins the game! Better luck next time!")
            else:
                print("🤝 The overall match is a tie!")
            print("Thanks for playing!")
            print("=======================================")
            break

        round_number += 1
        print()


if __name__ == "__main__":
    play_game()
