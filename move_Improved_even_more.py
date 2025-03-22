from main import *


def player_move(player_name, symbol):
    while True:
        print("\n> %s (%s), it's your turn!" % (player_name, symbol))
        square = int(input("> I'll choose number: "))

        row, column = Coordinates(square)

        if field[row][column] != "X" and field[row][column] != "O":
            return row, column

        print("\n> This square is already occupied! Please, choose another one.")
        """...we are checking if it's players or computers turn every time a player makes a wrong move [n]"""


def computer_move():
    while True:
        square = random.randint(1, 9)

        row, column = Coordinates(square)

        if field[row][column] != "X" and field[row][column] != "O":
            print("\n🖥️  Computer chose square number %s." % (square))
            return row, column


def Move(player_name, symbol):
    # player's turn:
    if player_name:
        row, column = player_move(player_name, symbol)
    # computer's turn
    else:
        row, column = computer_move()

    field[row][column] = symbol
    StylingTheField(field)