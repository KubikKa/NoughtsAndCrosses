import random


# Field for 'Noughts and crosses' game
def ClearField():
    field = [["1","2","3"],["4","5","6"],["7","8","9"]]
    return field


# Field styling
def StylingTheField(field):
    print("")
    print(" " + field[0][0] + " | " + field[0][1] + " | " + field[0][2] + " ")
    print("---.---.---")
    print(" " + field[1][0] + " | " + field[1][1] + " | " + field[1][2] + " ")
    print("---.---.---")
    print(" " + field[2][0] + " | " + field[2][1] + " | " + field[2][2] + " ")
    print("")


# Changing coordinates of the field's squares into simple numbers
def Coordinates(square):
    numbers = { 
        1: [0,0], 2: [0,1], 3: [0,2], 
        4: [1,0], 5: [1,1], 6: [1,2], 
        7: [2,0], 8: [2,1], 9: [2,2]
    }
    return numbers.get(square)


# Winning conditions
def WhoIsTheWinner(field):
    winners = {"X": crosses_player, "O": noughts_player}
    # checking rows
    for row in field:
        if row[0] == row[1] == row[2] in winners:
            print("%s is the winner!" %winners[row[2]])
            return True

    # checking columns
    columns = [[row[0] for row in field], [row[1] for row in field], [row[2] for row in field]]
    for i in range(len(columns)):
        if columns[i][0] == columns[i][1] == columns[i][2] in winners:
            print("%s is the winner!" %winners[columns[i][2]])
            return True

    # checking diagonals
    if field[0][0] == field[1][1] == field[2][2] in winners:
        print("%s is the winner!" %winners[field[2][2]])
        return True

    if field[2][0] == field[1][1] == field[0][2] in winners:
        print("%s is the winner!" %winners[field[0][2]])
        return True    
    return False


# Asking for names and choosing order
def NameAndOrder():
    while True:
        try:   
            choice2 = input("\n> If you want to decide who makes the move, press 1, if not, press 2: ").lower()         
            if choice2 == "2":
                name1 = input("\nFirst player name: ")
                name2 = input("Second player name: ")
                names = [name1, name2]
                if name1 == name2:
                    print("> Please, enter two different names to avoid confusion.")
                    continue
                else:
                    crosses_player = random.choice(names)
                    noughts_player = name1 if crosses_player == name2 else name2
                    return crosses_player, noughts_player
                
            elif choice2 == "1":
                crosses_player = input("\nCrosses player name: ")
                noughts_player = input("Noughts player name: ")
                if crosses_player == noughts_player:
                    print("> Please, enter two different names to avoid confusion.")
                    continue
                return crosses_player, noughts_player
            
            else:
                raise ValueError
        
        except:
            print("\n> Make sure you spell your answer correctly!")


# Selection of field squares
def Move(player_name, computer_name, symbol):
    while True:
        try:
            if player_name:
                print("\n> %s (%s), it's your turn!" %(player_name, symbol))
                square = int(input("> I'll choose number: "))
            else:
                square = random.randint(1, 9)
                
            row, column = Coordinates(square)

            if field[row][column] == "X" or field[row][column] == "O":
                if player_name:
                    print("\n> This square is already occupied! Please, choose another one.")
                continue
            else:
                if computer_name:
                    print("\n🖥️  Computer chose square number %s." %(square))
                field[row][column] = symbol   
                StylingTheField(field)
                break
        except:
            print("\n> There is no square with this number! Please try again and select number from 1-9.")


# Choose whether you want to play again
def PlayAgain():
    while True:
        game = input("\n> Do you want to play again? (Answer Y/N): ").lower()
        if game == "y":
            return True 
        elif game == "n":
            return False
        else:
            print("> Make sure you spell your answer correctly!")


# Main game loop
while True:
    text2 = """
> You can play this game with a friend (press 1) or the computer (press 2). It's up to you 😉
  Who do you want to play with?
"""
    print(text2)
    
    try:
        field = ClearField()
        available_moves = 9
        choice = int(input("> I choose option number: "))

        # playing with a friend
        if choice == 1:
            crosses_player, noughts_player = NameAndOrder()
            print("\n> Look, this is your field:")
            StylingTheField(field)

            while True:
                Move(crosses_player, "", "X")
                available_moves -= 1

                if WhoIsTheWinner(field):
                    break
                elif available_moves == 0:
                    print("It's a draw!")
                    break

                Move(noughts_player, "", "O")
                available_moves -= 1

                if WhoIsTheWinner(field):
                    break

        # playing with the computer
        elif choice == 2:
            while True:
                player_name = input("\nWhat's your name? ")
                computer_name = "Computer"
                names = [player_name, computer_name]
                if player_name == computer_name:
                    print("> Please, enter two different names to avoid confusion.")
                    continue
                else:
                    crosses_player = random.choice(names)
                    noughts_player = player_name if crosses_player == computer_name else computer_name
                    break
            
            text3 = """> Great, you chose a computer as your opponent!
  This is your field: 
"""
            print(text3)
            StylingTheField(field)

            while True:
                if crosses_player == computer_name:
                    Move("", computer_name, "X")
                else:
                    Move(crosses_player, "", "X")
                available_moves -= 1

                if WhoIsTheWinner(field):
                    break
                elif available_moves == 0:
                    print("It's a draw!")
                    break

                if noughts_player == computer_name:
                    Move("", computer_name, "O")
                else:
                    Move(noughts_player, "", "O")
                available_moves -= 1
            
                if WhoIsTheWinner(field):
                    break

        else:
            raise ValueError

    except:
        print("> Oops, make sure you chose the right number!")
        continue

    if not PlayAgain():
        break