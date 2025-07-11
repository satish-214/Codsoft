import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
#Rock-Paper-Scissors Game
        return 'user'
    else:
        return 'computer'

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print(" Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)

        if result == 'tie':
            print(" It's a tie!")
        elif result == 'user':
            print(" You win this round!")
            user_score += 1
        else:
            print(" Computer wins this round.")
            computer_score += 1
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        play_again = input("Play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nFinal Score - You:", user_score, "| Computer:", computer_score)
            print("Thanks for playing! Goodbye!")
            break
        round_number += 1
play_game()
