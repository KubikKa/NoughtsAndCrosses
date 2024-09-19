text1 = """
> Hi! You're playing a game called 'Noughts and crosses'.

> First, let's discuss the rules 📖:
1. Decide who will be noughts (O) and who will be crosses (X).
2. The player who chose crosses makes first move. You need to select a square (1-9) where you want to place the cross.
3. Next, the noughts player chooses another square to place the nought in it.
4. Both players continue to take turns to place their symbol in a square aiming to get three (X) or (O) in a row to win.
   Remember, you can not place your symbol in a square which is already occupied!
5. The three in a row can be in a horizontal, vertical or diagonal line.

> You can play this game with a friend (press 1) or the computer (press 2). It's up to you 😉
  Who do you want to play with?
"""
print(text1)

choice = int(input("I choose option number: "))

#wybór komputer/przyjaciel/źle wklepał
#wybór who's first

import random

#Field for 'Noughts and crosses' game
field = [["1","2","3"],["4","5","6"],["7","8","9"]]


#Field styling
def StylingTheField(field):
    print("")
    print(" " + field[0][0] + " | " + field[0][1] + " | " + field[0][2] + " ")
    print("---.---.---")
    print(" " + field[1][0] + " | " + field[1][1] + " | " + field[1][2] + " ")
    print("---.---.---")
    print(" " + field[2][0] + " | " + field[2][1] + " | " + field[2][2] + " ")
    print("")
    return 


#Changing coordinates of the field's squares into simple numbers
def Coordinates(square):
    numbers = { 
        1: [0,0], 2: [0,1], 3: [0,2], 
        4: [1,0], 5: [1,1], 6: [1,2], 
        7: [2,0], 8: [2,1], 9: [2,2]
    }
    return numbers.get(square)


#Conditions
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


available_moves = 9


#With a friend
if choice == 1:
    print("\n> Look, this is your field. Let the fun begin!")
    StylingTheField(field)

    while True:
        #Player's X turn
        while True:
            print("\n> Player X, it's your turn!")
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
                field[row][column] = "X"    
                StylingTheField(field)
                available_moves -= 1
                break


        if WhoIsTheWinner(field):
            break
        elif available_moves == 0:
            print("There is no winner!")
            break
        

        #Player's O turn 
        while True:
            print("\n> Player O, it's your turn!")
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
                field[row][column] = "O"    
                StylingTheField(field)
                available_moves -= 1
                break


        if WhoIsTheWinner(field):
            break


#With computer
elif choice == 2:
    text2 = """
> Great, you chose a computer as your opponent!
This is your field. Let the fun begin!
"""
    print(text2)
    StylingTheField(field)

    while True:
        #Player's X turn
        while True:
            print("\n> Dear player, it's your turn!")
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
                field[row][column] = "X"    
                StylingTheField(field)
                available_moves -= 1
                break


        if WhoIsTheWinner(field):
            break
        elif available_moves == 0:
            print("There is no winner!")
            break


        #Computer's turn
        while True:
            square = random.randint(1, 9)

            coordinates = Coordinates(square)
            row, column = coordinates

            if field[row][column] == "X" or field[row][column] == "O":
                continue
            else:
                field[row][column] = "O"
                print("\n* Computer chose square number %s." %(square))
                StylingTheField(field)
                available_moves -= 1
                break
    
        if WhoIsTheWinner(field):
            break


else:
    print("Upsi, I don't understand, please try again!")
# dokończ