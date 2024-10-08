text1 = """
> Hi! You're playing a game called 'Noughts and crosses'.

> First, let's discuss the rules 📖:
1. Enter your name (or names if you are playing with a friend) and the system will assign symbols - cross (x) or nought (O).
2. The first move is made by the player who gets the crosses. You need to select a square (1-9) where you want to place the cross.
3. Next, the noughts player chooses another square to place the nought in it.
4. Both players continue to take turns to place their symbol in a square aiming to get three (X) or (O) in a row to win.
   Remember, you can not place your symbol in a square which is already occupied!
5. The three in a row can be in a horizontal, vertical or diagonal line.
"""
print(text1)

import random

# Field for 'Noughts and crosses' game
field = [["1","2","3"],["4","5","6"],["7","8","9"]]


# Clear field - to reset the old one
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
def WhoIsTheWinner(field):                                                                  #too long, consider how you can change it
    if field[0][0] == "X" and field[0][1] == "X" and field[0][2] == "X":
        print("Player X is the winner!")
        return True
    elif field[0][0] == "O" and field[0][1] == "O" and field[0][2] == "O":
        print("Player O is the winner!")
        return True

    if field[1][0] == "X" and field[1][1] == "X" and field[1][2] == "X":
        print("Player X is the winner!")
        return True
    elif field[1][0] == "O" and field[1][1] == "O" and field[1][2] == "O":
        print("Player O is the winner!")
        return True

    if field[2][0] == "X" and field[2][1] == "X" and field[2][2] == "X":
        print("Player X is the winner!")
        return True
    elif field[2][0] == "O" and field[2][1] == "O" and field[2][2] == "O":
        print("Player O is the winner!")
        return True

    if field[0][0] == "X" and field[1][0] == "X" and field[2][0] == "X":
        print("Player X is the winner!")
        return True  
    elif field[0][0] == "O" and field[1][0] == "O" and field[2][0] == "O":
        print("Player O is the winner!")
        return True
    
    if field[0][1] == "X" and field[1][1] == "X" and field[2][1] == "X":
        print("Player X is the winner!")
        return True
    elif field[0][1] == "O" and field[1][1] == "O" and field[2][1] == "O":
        print("Player O is the winner!")
        return True

    if field[0][2] == "X" and field[1][2] == "X" and field[2][2] == "X":
        print("Player X is the winner!")
        return True
    elif field[0][2] == "O" and field[1][2] == "O" and field[2][2] == "O":
        print("Player O is the winner!")
        return True

    if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
        print("Player X is the winner!")
        return True
    elif field[0][0] == "O" and field[1][1] == "O" and field[2][2] == "O":
        print("Player O is the winner!")
        return True

    if field[2][0] == "X" and field[1][1] == "X" and field[0][2] == "X":
        print("Player X is the winner!")
        return True
    elif field[2][0] == "O" and field[1][1] == "O" and field[0][2] == "O":
        print("Player O is the winner!")
        return True
    return False


# Asking for names and choosing order
def NameAndOrder():
    while True:
        choice2 = input("\n> Do you want to decide who will make the first move? \n(Answer yes/no, if you do not want to make this decision, the computer will choose the order): ").lower()
        if choice2 == "no":
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
            
        elif choice2 == "yes":
            crosses_player = input("\nCrosses player name: ")
            noughts_player = input("Noughts player name: ")
            if crosses_player == noughts_player:
                print("> Please, enter two different names to avoid confusion.")
                continue
            return crosses_player, noughts_player
        
        else:
            print("Make sure you spell your answer correctly!")


# Each player's turn
def Player_turn(player_name, symbol):
    while True:
        print("\n> %s (%s), it's your turn!" %(player_name, symbol))
        square = int(input("> I'll choose number: "))

        if square < 1 or square > 9:
            print("\n> There is no square with this number! Please try again and select number from 1-9.")
            continue

        coordinates = Coordinates(square)
        row, column = coordinates 

        if field[row][column] == "X" or field[row][column] == "O":
            print("\n> This square is already occupied! Please, choose another one.")
            continue   
        else:
            field[row][column] = symbol    
            StylingTheField(field)
            break


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
        game = input("\n> Do you want to play again? (Answer yes/no): ").lower()
        if game == "yes":
            return True 
        elif game == "no":
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
    choice = int(input("> I choose option number: "))
    field = ClearField()
    available_moves = 9
# Playing with a friend
    if choice == 1:
        crosses_player, noughts_player = NameAndOrder()
        print("\n> Let the fun begin! Look, this is your field:")
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
Let the fun begin! This is your field: 
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

# Invalid input
    else:
        print("> Oopsi, make sure you chose the right number!")
        continue

    if not PlayAgain():
        break