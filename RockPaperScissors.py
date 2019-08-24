import random
import time

def game_check(player1, player2):
    # Return 0 if draw, 1 or 2 for which player wins
    # If computer it will be player 2
    winning_moves = {"rock": "scissors",
                     "scissors": "paper",
                     "paper": "rock"}
    
    player1 = str(player1).strip().lower()
    player2 = str(player2).strip().lower()
    try:
        if (player1 == player2):
            return 0
        elif (winning_moves[player1] == player2):
            return 1
        elif(winning_moves[player2] == player1):
            return 2
    except KeyError:
        return

def game_play(player1_play, player2_play = "", computer = False):
    if (computer):
        computer_play = random.choice(choices)
        if (game_check(player1_play, computer_play) == 0):
            print("Computer plays {}".format(computer_play))
            print("Tie!")
            time.sleep(5)
            print()
        elif (game_check(player1_play, computer_play) == 1):
            print("Computer plays {}".format(computer_play))
            print("Player wins!")
            time.sleep(5)
            print()
        elif (game_check(player1_play, computer_play) == 2):
            print("Computer plays {}".format(computer_play))
            print("Computer wins!")
            time.sleep(5)
            print()
        else:
            pass
    else:
        if (game_check(player1_play, player2_play) == 0):
            print("Player 1: {}, Player 2: {}".format(player1_play, player2_play))
            print("Tie!")
            time.sleep(5)
            print()
        elif (game_check(player1_play, player2_play) == 1):
            print("Player 1: {}, Player 2: {}".format(player1_play, player2_play))
            print("Player 1 wins!")
            time.sleep(5)
            print()
        elif (game_check(player1_play, player2_play) == 2):
            print("Player 1: {}, Player 2: {}".format(player1_play, player2_play))
            print("Player 2 wins!")
            time.sleep(5)
            print()
        else:
            pass

def game_menu():
    print("Welcome to Rock Paper Scissors!")
    print("Select an option below:")
    print()
    print("1. Play vs. computer")
    print("2. Play vs. player")
    print("3. Quit")
    print()

user_choice = "0"
while (user_choice != "3"):
    choices = ["rock","paper","scissors"]
    game_menu()
    user_choice = input("Selection: ")

    if (user_choice == "1"):
        user_play = ""
        while not(user_play.lower().strip() in choices):
            user_play = input("Enter rock, paper, or scissors: ")
        game_play(user_play, computer = True)

    elif (user_choice == "2"):
        user1_play = ""
        while not(user1_play.lower().strip() in choices):
            user1_play = input("Player 1 enter rock, paper, or scissors: ")
        user2_play = ""
        while not(user2_play.lower().strip() in choices):
            user2_play = input("Player 2 enter rock, paper, or scissors: ")
        print()
        game_play(user1_play, user2_play, computer = False)
    
    elif (user_choice == "3"):
        pass
    else:
        print("Please select an option.")
        print()


print()
print("Thank you for playing!")
