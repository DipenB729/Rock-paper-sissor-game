import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Player's choice
        player_choice = input("Enter your choice (0 for rock, 1 for paper, 2 for scissors): ")
        if player_choice not in ['0', '1', '2']:
            print("Invalid choice. Please enter 0 for rock, 1 for paper, or 2 for scissors.")
            continue
        
        player_choice = int(player_choice)
        
        # Computer's choice
        computer_choice = random.randint(0, 2)
        print(f"The computer chose: {computer_choice}")
        
        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 0 and computer_choice == 2) or \
             (player_choice == 1 and computer_choice == 0) or \
             (player_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("Computer wins!")
        
        # Ask for another round
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()
