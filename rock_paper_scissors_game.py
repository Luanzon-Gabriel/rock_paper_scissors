import random 

options = ("rock", "paper", "scissors")
running = True

player_name = input("Enter your name great warrior!:")

leaderboard = {"wins": 0, "losses": 0, "ties": 0}

rounds_played = 0

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        print("Choices are rock, paper, scissors only")
        player = input("Enter a choice (rock, paper, scissors): ").strip().lower()

    rounds_played += 1
    print(f"\nRound {rounds_played} - Player: {player}, Computer: {computer}")
    print(f"Player: {player}")
    print(f"Computer: {computer}")


    if player == computer:
            print("It's a tie!")
            leaderboard["ties"] += 1
    elif player == "rock" and computer == "scissors":
            print("You win!")
            leaderboard["wins"] += 1
    elif player == "paper" and computer == "rock":
            print("You win!")
            leaderboard["wins"] += 1
    elif player == "scissors" and computer == "paper":
            print("You win!")
            leaderboard["wins"] += 1
    else:
            print("You lose!")
            leaderboard["losses"] += 1

    print("\nLeaderboard:")
    print(f"Player: {player_name}")
    print(f"Wins: {leaderboard['wins']}")
    print(f"Losses: {leaderboard['losses']}")
    print(f"Ties: {leaderboard['ties']}")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
                    running = False

print("\nFinal Leaderboard:")
print(f"Player: {player_name}")
print(f"Wins: {leaderboard['wins']}")
print(f"Losses: {leaderboard['losses']}")
print(f"Ties: {leaderboard['ties']}")
print(f"Total Rounds Played: {rounds_played}")