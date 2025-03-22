from main import *


def Move(player_name, symbol):
    # player's turn:
    if player_name:
        while True:
            print("\n> %s (%s), it's your turn!" % (player_name, symbol))
            square = int(input("> I'll choose number: "))

            row, column = Coordinates(square)

            if field[row][column] == "X" or field[row][column] == "O":
                print("\n> This square is already occupied! Please, choose another one.")
                """...we are checking if it's players or computers turn every time a player makes a wrong move [n]"""
                continue
            break

    # computer's turn
    else:
        while True:
            square = random.randint(1, 9)

            row, column = Coordinates(square)

            if field[row][column] == "X" or field[row][column] == "O":
                continue
            print("\n🖥️  Computer chose square number %s." % (square))
            break

    field[row][column] = symbol
    StylingTheField(field)