"""
print("⭕✖️")
"""


#Field for 'Noughts and cross' game
field = [[" "," "," "],[" "," "," "],[" "," "," "]]


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
    return numbers.get(square)                                                          #bo TypeError: 'dict' object is not callable



print("\nLook at this field. You have 9 squares which you can occupy.")
StylingTheField(field)                                                                  #add numbers czy coś, bo skąd mają wiedzieć który kwadracik to który



#Player's X turn
while True:
    print("\n> Player X, it's your turn. Please select the number (1-9) of the square you want to occupy. \nBut do not choose the square which is already taken.")
    square = int(input("\n> I'll choose number: "))

    if square < 1 or square > 9:
        print("\n> There is no square with this number! Please try again and select number from 1-9.") #wywala błąd, coś tam rows and columns, trzeba wyświetlić print
        

    coordinates = Coordinates(square)
    row, column = coordinates 


    if field[row][column] != " ":
        print("\n> This square is already occupied! Please, choose another one.")
        square = int(input("\n> I'll choose a square number: "))                             

    else:
        field[row][column] = "X"    
        StylingTheField(field)
        break

    

#Player's O turn 
while True:                                                                
    print("\n> Player O, it's your turn. Please select the number (1-9) of the square you want to occupy. \nBut do not choose the square which is already taken.")
    square = int(input("\n> I'll choose number: "))

    if square < 1 or square > 9:
        print("\n> There is no square with this number! Please try again and select number from 1-9.")   #wywala błąd, coś tam rows and columns, trzeba wyświetlić print
        

    coordinates = Coordinates(square)
    row, column = coordinates 


    if field[row][column] != " ":
        print("\n> This square is already occupied! Please, choose another one.")
        square = int(input("\n> I'll choose a square number: "))                             #wprowadzasz popr., wyskakuje pierwszy print zamiast plan.

    else:
        field[row][column] = "O"    
        StylingTheField(field)
        break