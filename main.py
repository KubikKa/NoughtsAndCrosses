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
    return 


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
    # checking rows
    for row in field:
        if row[0] == row[1] == row[2] == "X":
            print("Player %s is the winner!" %crosses_player)
            return True
        elif row[0] == row[1] == row[2] == "O":
            print("Player %s is the winner!" %noughts_player)
            return True

    # checking columns
    columns = [[row[0] for row in field], [row[1] for row in field], [row[2] for row in field]]
    for i in range(len(columns)):
        if columns[i][0] == columns[i][1] == columns[i][2] == "X":
            print("Player %s is the winner!" %crosses_player)
            return True
        elif columns[i][0] == columns[i][1] == columns[i][2] == "O":
            print("Player %s is the winner!" %noughts_player)
            return True

    # checking diagonals
    if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
        print("Player %s is the winner!" %crosses_player)
        return True
    elif field[0][0] == "O" and field[1][1] == "O" and field[2][2] == "O":
        print("Player %s is the winner!" %noughts_player)
        return True

    if field[2][0] == "X" and field[1][1] == "X" and field[0][2] == "X":
        print("Player %s is the winner!" %crosses_player)
        return True
    elif field[2][0] == "O" and field[1][1] == "O" and field[0][2] == "O":
        print("Player %s is the winner!" %noughts_player)
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


# Each player's turn
def Player_turn(player_name, symbol):
    while True:
        print("\n> %s (%s), it's your turn!" %(player_name, symbol))

        try:
            square = int(input("> I'll choose number: "))
            coordinates = Coordinates(square)
            row, column = coordinates 

            if field[row][column] == "X" or field[row][column] == "O":
                print("\n> This square is already occupied! Please, choose another one.")
                continue   
            else:
                field[row][column] = symbol    
                StylingTheField(field)
                break
        except:
            print("\n> There is no square with this number! Please try again and select number from 1-9.")
            continue


# Computer's turn
def Computer(symbol):
    while True:
        square = random.randint(1, 9)

        coordinates = Coordinates(square)
        row, column = coordinates

        if field[row][column] == "X" or field[row][column] == "O":
            continue
        else:
            field[row][column] = symbol
            print("\n🖥️  Computer chose square number %s." %(square))
            StylingTheField(field)
            break


# Choose whether you want to play again
def PlayAgain():
    while True:
        game = input("\n> Do you want to play again? (Answer Y/N): ").lower()
        
        try:
            if game == "y":
                return True 
            elif game == "n":
                return False
            else:
                raise ValueError
        
        except:
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
        # Playing with a friend
        if choice == 1:
            crosses_player, noughts_player = NameAndOrder()
            print("\n> Look, this is your field:")
            StylingTheField(field)

            while True:
                Player_turn(crosses_player, "X")
                available_moves -= 1

                if WhoIsTheWinner(field):
                    break
                elif available_moves == 0:
                    print("There is no winner!")
                    break

                Player_turn(noughts_player, "O")
                available_moves -= 1

                if WhoIsTheWinner(field):
                    break

        # Playing with the computer
        elif choice == 2:
            while True:
                player_name = input("\nWhat's your name? ")
                computer_name = "Computer"
                names = [player_name, computer_name]
                if player_name == computer_name:
                    print("> Please, please enter two different names to avoid confusion.")
                    continue
                else:
                    crosses_player = random.choice(names)
                    noughts_player = player_name if crosses_player == computer_name else computer_name
                    break
            
            text3 = """
    > Great, you chose a computer as your opponent!
    This is your field: 
    """
            print(text3)
            StylingTheField(field)

            while True:
                if crosses_player == computer_name:
                    Computer("X")
                else:
                    Player_turn(crosses_player, "X")
                available_moves -= 1

                if WhoIsTheWinner(field):
                    break
                elif available_moves == 0:
                    print("There is no winner!")
                    break

                if noughts_player == computer_name:
                    Computer("O") 
                else:
                    Player_turn(noughts_player, "O")
                available_moves -= 1
            
                if WhoIsTheWinner(field):
                    break

        else:
            raise ValueError

    # Invalid input
    except:
        print("> Oopsi, make sure you chose the right number!")
        continue

    if not PlayAgain():
        break