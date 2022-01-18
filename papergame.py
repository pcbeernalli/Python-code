import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    players = None

    while players not in choices:
        players = input("rock,paper,or scissors?:").lower()
    if players == computer:
        print("computer:",computer)
        print("players:",players)
        print("tie!")
    elif players == "rock":
        if computer == "paper":
            print("computer:", computer)
            print("players:", players)
            print("you lose")
        if computer == "scissors":
            print("computer:", computer)
            print("players:", players)
            print("you win")
    elif players == "paper":
        if computer == "rock":
            print("computer:", computer)
            print("players:", players)
            print("you lose")
        if computer == "scissors":
            print("computer:", computer)
            print("players:", players)
            print("you win")
    elif players == "scissors":
        if computer == "paper":
            print("computer:", computer)
            print("players:", players)
            print("you lose")
        if computer == "rock":
            print("computer:", computer)
            print("players:", players)
            print("you win")

    play_again = input("play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("bye!")