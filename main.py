import random

def main():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock! 🪨 📄 ✂️ 🦎 🖖")
    choices = ["rock", "paper", "scissors", "lizard", "spock"]

    while True:
        print_options(choices)
        user_choice = input("Enter your choice: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please enter a valid option. ❌")
            continue

        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie! 😐")
        elif (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
             (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
             (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
             (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
             (user_choice == "spock" and (computer_choice == "rock" or computer_choice == "scissors")):
            print("You win! 🎉")
        else:
            print("Computer wins! 💻")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye! 👋💔😢")
            break

def print_options(options):
    print("Choose your option:")
    for idx, option in enumerate(options, start=1):
        emoji = "🪨" if option == "rock" else "📄" if option == "paper" else "✂️" if option == "scissors" else "🦎" if option == "lizard" else "🖖"
        print(f"{idx}. {option.capitalize()} {emoji}")

if __name__ == "__main__":
    main()
