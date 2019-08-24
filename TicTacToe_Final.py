def print_board(gBoard):
    for row in gBoard:
        print(row)

def check_board(gBoard):
    diag_right_wins = []
    # Top left to bottom right diagonal check
    for x in range(1, len(gBoard)):
        diag_right_wins.append(gBoard[x-1][x-1] == gBoard[x][x] !=0)
    if not(False in diag_right_wins):
        return True
    # Bottom left to top right diagonal check
    diag_left_wins = []
    for x in range(len(gBoard)-1,0,-1):
        diag_left_wins.append(gBoard[len(gBoard) - (x + 1)][x] == gBoard[len(gBoard) - x][x-1] != 0)
    if not(False in diag_left_wins):
        return True
    # Rows check
    for row in gBoard:
        if (len([x for x in row if x == row[0] != 0]) == len(row)):
            return True
    # Columns check
    for col in range(0, len(gBoard)):
        col_wins = []
        for row in range(1, len(gBoard)):
            col_wins.append(gBoard[row-1][col] == gBoard[row][col] != 0)
        if not(False in col_wins):
            return True
    return False

def check_tie(gBoard):
    for row in gBoard:
        for num in row:
            if num == 0:
                return False
    return True

'''Dynamic game board'''
game_size = 3
game_board = [[0 for x in range(game_size)] for x in range(game_size)]
'''Should probably put a cap on size, maybe 10 X 10'''

# Begin the game
'''Could have loop here for user to set game size'''
end_game = False
player = 0
while not (end_game):
    if (check_board(game_board)):
        end_game = True
        continue
    elif (check_tie(game_board)):
        end_game = True
        continue
    else:
        # Player turn start, set player
        player_turn_over = False
        if (player == 1):
            player = 2
        else:
            player = 1
        while not (player_turn_over):
            player_row = int 
            player_col = int
            print()
            print_board(game_board)
            print()
            while (player_row not in range(game_size)):
                try:
                    player_row = int(input(f"Player {player}, enter row: "))
                except ValueError:
                    continue
            while (player_col not in range(game_size)):
                try:
                    player_col = int(input(f"Player {player}, enter column: "))
                except ValueError:
                    continue
            if (game_board[player_row][player_col] != 0):
                print()
                print(f"Position already taken, try again player {player}.")
                
            else:
                game_board[player_row][player_col] = player
                player_turn_over = True

if (check_tie(game_board)):
    print()
    print_board(game_board)
    print()
    print("Tie game, no winners.")
else:
    print()
    print_board(game_board)
    print()
    print("Player",player,"wins!!!")
