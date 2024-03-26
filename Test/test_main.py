import random

def play(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
         (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
         (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
         (user_choice == "spock" and (computer_choice == "rock" or computer_choice == "scissors")):
        return "You win!"
    else:
        return "Computer wins!"

def test_play():
    assert play("rock", "rock") == "It's a tie!"
    assert play("rock", "paper") == "Computer wins!"
    assert play("rock", "scissors") == "You win!"
    assert play("rock", "lizard") == "You win!"
    assert play("rock", "spock") == "Computer wins!"

    assert play("paper", "paper") == "It's a tie!"
    assert play("paper", "rock") == "You win!"
    assert play("paper", "scissors") == "Computer wins!"
    assert play("paper", "lizard") == "Computer wins!"
    assert play("paper", "spock") == "You win!"

    assert play("scissors", "scissors") == "It's a tie!"
    assert play("scissors", "rock") == "Computer wins!"
    assert play("scissors", "paper") == "You win!"
    assert play("scissors", "lizard") == "You win!"
    assert play("scissors", "spock") == "Computer wins!"

    assert play("lizard", "lizard") == "It's a tie!"
    assert play("lizard", "rock") == "Computer wins!"
    assert play("lizard", "paper") == "You win!"
    assert play("lizard", "scissors") == "Computer wins!"
    assert play("lizard", "spock") == "You win!"

    assert play("spock", "spock") == "It's a tie!"
    assert play("spock", "rock") == "You win!"
    assert play("spock", "paper") == "Computer wins!"
    assert play("spock", "scissors") == "You win!"
    assert play("spock", "lizard") == "Computer wins!"

if __name__ == "__main__":
    test_play()
    print("All tests passed!")
