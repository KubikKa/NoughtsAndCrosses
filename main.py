import random


# Board for 'Noughts and crosses' game
def clear_board():
    board = [["1","2","3"],["4","5","6"],["7","8","9"]]
    return board


# Display the current board
"""a bit repetitive, could be put in a loop. You can use \n instead of printing black lines [n]"""
def display_board(board):
    print("")
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---.---.---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---.---.---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
    print("")


# Changing coordinates of the board's squares into simple numbers
"""is this function even needed? [s]"""
def get_coordinates(square):
    numbers = {
        1: [0,0], 2: [0,1], 3: [0,2], 
        4: [1,0], 5: [1,1], 6: [1,2], 
        7: [2,0], 8: [2,1], 9: [2,2]
    }
    return numbers[square]


# Winning conditions
def who_is_the_winner(board):
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


# Asking for names and choosing order
def name_and_order():
    while True:
        choice = input("\n> If you want to decide who makes the move, press 1, if not, press 2: ").lower()
        if choice not in ("1", "2"):
            print("\n> Make sure you spell your answer correctly!")
            continue

        if choice == "2":
            name1 = input("\nFirst player name: ")
            name2 = input("Second player name: ")
            if name1 == name2:
                print("> Please, enter two different names to avoid confusion.")
                continue
            crosses_player = random.choice((name1, name2))
            noughts_player = name1 if crosses_player == name2 else name2
            return crosses_player, noughts_player

        else:
            """Some parts of the code here are repeated from the previous if statement, they could be put in a function [n]"""
            crosses_player = input("\nCrosses player name: ")
            noughts_player = input("Noughts player name: ")
            if crosses_player == noughts_player:
                print("> Please, enter two different names to avoid confusion.")
                """Continue jumps to the next loop, thus executing all of the above code [s]"""
                continue
            return crosses_player, noughts_player


# Selection of board squares
"""This function is too broad. it combines handling input, validating it, board updates, display and logic (bad separation of concerns) [m]"""
def move(player_name, computer_name, symbol):
    while True:
        try:
            if player_name:
                """smart use of truthyness / falsyness [+]"""
                """if the symbol:name dict was a variable in the higher namespace it could be used here [n]"""
                print("\n> %s (%s), it's your turn!" %(player_name, symbol))
                square = int(input("> I'll choose number: "))
            else:
                """
                could be optimised, the computer will be calling this over and over again repeating the whole loop
                until it finds an empty value [s]"""
                square = random.randint(1, 9)
                
            row, column = get_coordinates(square)

            if board[row][column] == "X" or board[row][column] == "O":
                if player_name:
                    print("\n> This square is already occupied! Please, choose another one.")
                """...we are checking if it's players or computers turn every time a player makes a wrong move [n]"""
                continue
            else:
                if computer_name:
                    print("\n🖥️  Computer chose square number %s." %(square))
                board[row][column] = symbol   
                display_board(board)
                break
        except:
            """broad exception again [n]"""
            print("\n> There is no square with this number! Please try again and select number from 1-9.")


# Choose whether you want to play again
def play_again():
    while True:
        restart_decision = input("\n> Do you want to play again? (Answer Y/N): ").lower()
        if restart_decision == "y":
            return True 
        elif restart_decision == "n":
            return False
        print("> Make sure you spell your answer correctly!")


# Main game loop
while True:
    print("> You can play this game with a friend (press 1) or the computer (press 2). It's up to you 😉\n  Who do you want to play with?")
    board = clear_board()
    """does it really have to be a separate variable? the board itself already stores this information, you just need to retrieve it [s]"""
    available_moves = 9

    choice = input("> I choose option number: ")
    if choice not in ("1", "2"):
        print("> Oops, make sure you chose the right number!")
        continue

    # playing with a friend
    """you put the user selection of name and order in a separate function, why put the choice of gamemode in the main loop? [s]"""
    if choice == "1":
        crosses_player, noughts_player = name_and_order()
        print("\n> Look, this is your board:")
        display_board(board)

        while True:
            move(crosses_player, "", "X")
            available_moves -= 1

            if who_is_the_winner(board):
                break
            elif available_moves == 0:
                print("It's a draw!")
                break

            move(noughts_player, "", "O")
            available_moves -= 1

            if who_is_the_winner(board):
                break

    # playing with the computer
    else:
        while True:
            player_name = input("\nWhat's your name? ")
            """computer_name is a constant"""
            computer_name = "Computer"
            if player_name == computer_name:
                print("> Please, enter two different names to avoid confusion.")
                continue

            crosses_player = random.choice((player_name, computer_name))
            noughts_player = player_name if crosses_player == computer_name else computer_name
            break
        
        print("\n> Great, you chose a computer as your opponent!\n  This is your board:")
        display_board(board)

        while True:
            """you are checking which player is playing as what symbol every turn [s]"""
            if crosses_player == computer_name:
                move("", computer_name, "X")
            else:
                move(crosses_player, "", "X")
            available_moves -= 1

            if who_is_the_winner(board):
                break
            elif available_moves == 0:
                print("It's a draw!")
                break

            if noughts_player == computer_name:
                move("", computer_name, "O")
            else:
                move(noughts_player, "", "O")
            available_moves -= 1
        
            if who_is_the_winner(board):
                break

    if not play_again():
        break


""""
2. za dużo używania globalnych zmiennych w funkcjach. jest to niebezpieczne. Lepiej przekazywać je funkcjom jako argumenty

guard clauses
"""