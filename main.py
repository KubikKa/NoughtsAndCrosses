import random


# Initialises and returns a fresh 3x3 board
def clear_board():
    board = [["1","2","3"],["4","5","6"],["7","8","9"]]
    return board


# Renders the current state of board to the console for the player
def display_board(board):
    print()
    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2] + " ")
        if i < 2:
            print("---.---.---")
    print()


# Converts a square number to its corresponding indices on the board
def get_coordinates(square):
    numbers = {
        1: [0,0], 2: [0,1], 3: [0,2], 
        4: [1,0], 5: [1,1], 6: [1,2], 
        7: [2,0], 8: [2,1], 9: [2,2]
    }
    return numbers[square]


# Checks the current board for winning condition. 
# If a player has won, returns True and announces the winner; otherwise, returns False
def who_is_the_winner(board, crosses_player, noughts_player):
    winners = {"X": crosses_player, "O": noughts_player}

    for i in range(3):
        # checking rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] in winners:
            print("%s is the winner!" %winners[board[i][0]])
            return True
        #checking columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] in winners:
            print("%s is the winner!" %winners[board[0][i]])
            return True
    
    # checking diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in winners:
        print("%s is the winner!" %winners[board[0][0]])
        return True

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] in winners:
        print("%s is the winner!" %winners[board[2][0]])
        return True
    return False


# Retrives player's names, ensuring they are distinct
def get_names(first_prompt, second_prompt):
    while True:
        player_one = input(first_prompt)
        player_two = input(second_prompt)
        if player_one != player_two:
            return player_one, player_two
        print("> Please, enter two different names to avoid confusion.")


# Determines which player uses "X" and which uses "O" based on their choice or random assignment
def name_and_order():
    while True:
        choice = input("\n> If you want to decide who makes the move, press 1, if not, press 2: ").lower()
        if choice not in ("1", "2"):
            print("\n> Make sure you spell your answer correctly!")
            continue

        if choice == "2":
            name1, name2 = get_names("\nFirst player name: ", "Second player name: ")
            crosses_player = random.choice((name1, name2))
            noughts_player = name1 if crosses_player == name2 else name2
            return crosses_player, noughts_player

        else:
            crosses_player, noughts_player = get_names("\nCrosses player name: ", "Noughts player name: ")
            return crosses_player, noughts_player


# Handles the process of human player selecting a square
def player_move(player_name, symbol, board):
    while True:
        print("\n> %s (%s), it's your turn!" %(player_name, symbol))
        try:
            square = int(input("> I'll choose number: "))

            row, column = get_coordinates(square)

            if board[row][column] in ("X", "O"):
                print("\n> This square is already occupied! Please, choose another one.")
                continue

        except (KeyError, ValueError):
            print("\n> There is no square with this number! Please try again and select number from 1-9.")
            continue
        
        return row, column
    

# Selects a free square for computer's move by drawing an avaliable random number from the range 1-9
def computer_move(board):
    while True:
        square = random.randint(1, 9)
        row, column = get_coordinates(square)

        if board[row][column] in ("X", "O"):
            continue

        print("\n🖥️  Computer chose square number %s." %(square))
        return row, column


# Places the player's or computer symbol on the board and updates the display
def move(player_name, symbol, board):
    if player_name:
        row, column = player_move(player_name, symbol, board)
    else:
        row, column = computer_move(board)

    board[row][column] = symbol    
    display_board(board)


# Prompts the user to decide whether to start a new game
def play_again():
    while True:
        restart_decision = input("\n> Do you want to play again? (Answer Y/N): ").lower()
        if restart_decision == "y":
            return True 
        elif restart_decision == "n":
            return False
        print("> Make sure you spell your answer correctly!")


# Prompts the user to choose between playing against another person or the computer
def get_game_mode():
    while True:
        print("> You can play this game with a friend (press 1) or the computer (press 2). It's up to you 😉\n  Who do you want to play with?")
        mode = input("> I choose option number: ")
        if mode in ("1", "2"):
            return mode
        print("> Oops, make sure you chose the right number!")
        

# Sets players names and assings symbols depending on the selected game mode
def setup_players(mode):
    if mode == "1":
        return name_and_order()
    else:
        while True:
            player_name = input("\nWhat's your name? ")
            computer_name = "Computer"
            if player_name == computer_name:
                print("> Please, enter two different names to avoid confusion.")
                continue

            crosses_player = random.choice((player_name, computer_name))
            noughts_player = player_name if crosses_player == computer_name else computer_name
            return crosses_player, noughts_player


# Assigns player depending on the selected game mode
# Returns player's name unless mode 2 is selected and it's the Computer's turn
def get_player_for_turn(mode, name):
    if mode == "2" and name == "Computer":
        return None
    else:
        return name


# ---------- MAIN GAME LOOP ----------
while True:
    board = clear_board()
    available_moves = 9

    game_mode = get_game_mode()
    crosses_player, noughts_player = setup_players(game_mode)

    print("\n> Look, this is your board:")
    display_board(board)

    # Handle gameplay
    while True:
        move(get_player_for_turn(game_mode, crosses_player), "X", board)
        available_moves -= 1

        if who_is_the_winner(board, crosses_player, noughts_player):
            break
        elif available_moves == 0:
            print("It's a draw!")
            break

        move(get_player_for_turn(game_mode, noughts_player), "O", board)
        available_moves -= 1

        if who_is_the_winner(board, crosses_player, noughts_player):
            break

    if not play_again():
        break