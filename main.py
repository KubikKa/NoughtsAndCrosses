"""
print("⭕✖️")
"""


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


text1 = """
> Hi! You're playing a game called 'Noughts and crosses'.
You can play it with a friend or the computer. It's up to you 😉

> First, let's discuss the rules:
1. Decide who will be noughts (O) and who will be crosses (X).
2. The player who chose crosses makes first move. Select a square where you want to place the cross.
3. Next, the noughts player chooses another square to place the nought in it.
4. Both players continue to take turns to place their symbol in a square aiming to get three (X) or (O) in a row to win.
   Remember, you can not place your symbol in a square which is already occupied!
5. The three in a row can be in a horizontal, vertical or diagonal line.

There is your field!
"""

print(text1)
StylingTheField(field)

text2 = """
Now please answer these questions:
"""
#wybór komputer/przyjaciel
#wybór who's first
print(text2)


#Player's X turn
while True:
    print("\n> Player X, it's your turn! Select a number of the square where you want to place the cross.")
    square = int(input("\n> I'll choose number: "))

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
        break

    

#Player's O turn 
while True:                                                                
    print("\n> Player O, it's your turn! Select a number of the square where you want to place the nought.")
    square = int(input("\n> I'll choose number: "))

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
        break