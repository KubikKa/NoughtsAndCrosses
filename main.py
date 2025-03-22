"""
Rated with comments
[+] - something very positive

[n] - nitpick
[s] - small issue
[m] - medium issue
[!] - major issue
- Y
"""

import random


# Field for 'Noughts and crosses' game
"""snake_case for functions, PascalCase for classes [n]"""
def ClearField():
    field = [["1","2","3"],["4","5","6"],["7","8","9"]]
    return field


# Field styling
"""a bit repetitive, could be put in a loop. You can use \n instead of printing black lines [n]"""
"""unhelpful function name, 'style' could be understood as 'change how it looks', but the function displays the field [n]"""
def StylingTheField(field):
    print("")
    print(" " + field[0][0] + " | " + field[0][1] + " | " + field[0][2] + " ")
    print("---.---.---")
    print(" " + field[1][0] + " | " + field[1][1] + " | " + field[1][2] + " ")
    print("---.---.---")
    print(" " + field[2][0] + " | " + field[2][1] + " | " + field[2][2] + " ")
    print("")


# Changing coordinates of the field's squares into simple numbers
"""good use of dictionaries [+], but name could be more descriptive (eg. get_coordinates) [n]. Why is is called square?"""
"""is this function even needed? [s]"""
def Coordinates(square):
    numbers = { 
        1: [0,0], 2: [0,1], 3: [0,2], 
        4: [1,0], 5: [1,1], 6: [1,2], 
        7: [2,0], 8: [2,1], 9: [2,2]
    }
    """why use .get() instead of numbers[square]? [n]"""
    """the difference: [] throws a KeyError, get returns None when key is missing"""
    return numbers.get(square)


# Winning conditions
def WhoIsTheWinner(field):
    winners = {"X": crosses_player, "O": noughts_player}
    # checking rows
    """good method for checking rows [+]"""
    for row in field:
        if row[0] == row[1] == row[2] in winners:
            print("%s is the winner!" %winners[row[2]])
            return True

    # checking columns
    """
    good use of string comprehension [+]
    but is it necessary?
    you iterate unnecessary number of times, adding overhead
    creating unnecessary variables (columns) [m]
    """
    columns = [[row[0] for row in field], [row[1] for row in field], [row[2] for row in field]]
    """
    The whole for loop here is basically the same as in the part that checks rows, it could be put in a function
    to avoid repetition [n]
    """
    for i in range(len(columns)):
        if columns[i][0] == columns[i][1] == columns[i][2] in winners:
            print("%s is the winner!" %winners[columns[i][2]])
            return True

    # checking diagonals
    """Could be put into one if statement with the use of 'or' operator [n]"""
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
            """Why choice2? where's choice1? xd"""
            choice2 = input("\n> If you want to decide who makes the move, press 1, if not, press 2: ").lower()         
            if choice2 == "2":
                name1 = input("\nFirst player name: ")
                name2 = input("Second player name: ")
                """why define the variables and then put them in a separate list duplicating these variables? [s]"""
                names = [name1, name2]
                if name1 == name2:
                    print("> Please, enter two different names to avoid confusion.")
                    continue
                else:
                    crosses_player = random.choice(names)
                    noughts_player = name1 if crosses_player == name2 else name2
                    return crosses_player, noughts_player

            elif choice2 == "1":
                """Some parts of the code here are repeated from the previous if statement, they could be put in a function [n]"""
                crosses_player = input("\nCrosses player name: ")
                noughts_player = input("Noughts player name: ")
                if crosses_player == noughts_player:
                    print("> Please, enter two different names to avoid confusion.")
                    """Continue jumps to the next loop, thus executing all of the above code [s]"""
                    continue
                """inconsistency: you put else: before but not now"""
                return crosses_player, noughts_player
            
            else:
                raise ValueError
        
        except:
            """except what? [n]"""
            print("\n> Make sure you spell your answer correctly!")


# Selection of field squares
"""This function is too broad. it combines handling input, validating it, field updates, display and logic (bad separation of concerns) [m]"""
def Move(player_name, computer_name, symbol):
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
                
            row, column = Coordinates(square)

            if field[row][column] == "X" or field[row][column] == "O":
                if player_name:
                    print("\n> This square is already occupied! Please, choose another one.")
                """...we are checking if it's players or computers turn every time a player makes a wrong move [n]"""
                continue
            else:
                if computer_name:
                    print("\n🖥️  Computer chose square number %s." %(square))
                field[row][column] = symbol   
                StylingTheField(field)
                break
        except:
            """broad exception again [n]"""
            print("\n> There is no square with this number! Please try again and select number from 1-9.")


# Choose whether you want to play again
def PlayAgain():
    while True:
        """vague variable name, consider something like 'should_restart' or 'restart_decision' or 'user_choice' [n]"""
        game = input("\n> Do you want to play again? (Answer Y/N): ").lower()
        if game == "y":
            return True 
        elif game == "n":
            return False
        else:
            """this else is unnecessary [n]"""
            print("> Make sure you spell your answer correctly!")


# Main game loop
while True:
    """vague variable names, does it even need to be a separate variable? [n]"""
    text2 = """
> You can play this game with a friend (press 1) or the computer (press 2). It's up to you 😉
  Who do you want to play with?
"""
    print(text2)
    
    try:
        field = ClearField()
        """does it really have to be a separate variable? the field itself already stores this information, you just need to retrieve it [s]"""
        available_moves = 9
        """
        try / except should be as small as possible to only handle the part they are concerned about, this whole huge try / except statement
        should only really cover this single line [S]
        """
        choice = int(input("> I choose option number: "))

        # playing with a friend
        """you put the user selection of name and order in a separate function, why put the choice of gamemode in the main loop? [s]"""
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

                """Good you didn't check for a draw again because it would be unnecessary [+]"""
                if WhoIsTheWinner(field):
                    break

        # playing with the computer
        elif choice == 2:
            while True:
                player_name = input("\nWhat's your name? ")
                """computer_name is a constant"""
                computer_name = "Computer"
                names = [player_name, computer_name]
                """why define the variables and then put them in a separate list duplicating these variables? [s]"""
                if player_name == computer_name:
                    print("> Please, enter two different names to avoid confusion.")
                    continue
                else:
                    """this else is unnecessary [n]"""
                    crosses_player = random.choice(names)
                    noughts_player = player_name if crosses_player == computer_name else computer_name
                    break
            
            text3 = """> Great, you chose a computer as your opponent!
  This is your field: 
"""
            print(text3)
            StylingTheField(field)

            while True:
                """you are checking which player is playing as what symbol every turn [s]"""
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
        """Except what? [n]"""
        print("> Oops, make sure you chose the right number!")
        continue

    if not PlayAgain():
        break


""""
wnioski:
[+]: 5
[n]: 17
[s]: 9
[m]: 2

1. tworzysz jakąś strukturę danych i zamiast się jej trzymać, to gdy napotkujesz jakiś problem, konwertujesz ją do innej
postaci i potem pracujesz na niej zamiast trzymać się tego co już masz.

2. za dużo używania globalnych zmiennych w funkcjach. jest to niebezpieczne. Lepiej przekazywać je funkcjom jako argumenty

guard clauses
"""