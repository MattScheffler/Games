import string
import random

# First import the dictionary of words and set a random one to play with
file = "Dictionary.txt"
dictionary_words = []

with open(file) as f:
    f_line = f.readline()
    while (f_line):
        f_line = f_line.strip()
        dictionary_words.append(f_line)
        f_line = f.readline()

random_word_number = random.randint(0,len(dictionary_words))
random_word = dictionary_words[random_word_number]

# Function for printing out the board that letters and spaces appear on
def print_board(g_board):
    for letter in range(0,len(g_board)-1):
        print(g_board[letter], end=" ")
    print(g_board[len(g_board)-1])

# Track the letters the player has guessed, and number of guesses
guessed_letters = []
player_guess_count = 0

print("Welcome to Hangman!")
print("")
print("Number of letters:", len(random_word))
game_board = []
for letter in random_word:
    game_board.append("_")

# Start the game here
print_board(game_board)

while("_" in game_board):
    if (player_guess_count == 6):
        break
    print("Letters guessed:", sorted(guessed_letters))
    print("Remaining guesses:", (6 - player_guess_count))
    print("")
    player_guess = input("Guess a letter: ").upper()
    if (len(player_guess) != 1):
        print("")
        print("Please only enter one letter")
        player_guess_count += 1
    elif (player_guess in guessed_letters):
        print("")
        print("That letter has already been guessed!")
        player_guess_count += 1
    elif (player_guess not in string.ascii_uppercase):
        print("")
        print("Please only enter single letters, no numbers or symbols.")
        player_guess_count += 1
    else:
        good_guess = False
        x = -1
        for letter in random_word:
            x += 1
            if player_guess == letter:
                game_board[x] = letter
                good_guess = True
        guessed_letters.append(player_guess)
        if not(good_guess):
            player_guess_count += 1
    print("")
    print_board(game_board)

if (player_guess_count == 6):
    print("You lose.")
else:
    print("You win!")
