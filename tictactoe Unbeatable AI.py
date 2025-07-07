import random
def Setuptable():
    Winner = False
    Gameend = False
    Table = [[" " for i in range(8)] for j in range(8)]
    Input = int(input("Input 1 to be the first player (X) or 2 to be the second player (O): "))
    while Input != 1 and Input != 2:
        Input = input("Your options are 1 or 2: ")
    if Input == 1:
        player = "X"
        robot = "O"
    if Input == 2:
        robot = "X"
        player = "O"
    Table[0][0] = 3
    Table[2][0] = 2
    Table[4][0] = 1
    Table[5][1] = 1
    Table[5][3] = 2
    Table[5][5] = 3
    Table[1][1] = "-"
    Table[3][1] = "-"
    Table[1][3] = "-"
    Table[1][5] = "-"
    Table[3][3] = "-"
    Table[3][5] = "-"
    Table[3][4] = "|"
    Table[4][4] = "|"
    Table[2][4] = "|"
    Table[1][4] = "|"
    Table[0][4] = "|"
    Table[3][2] = "|"
    Table[4][2] = "|"
    Table[2][2] = "|"
    Table[1][2] = "|"
    Table[0][2] = "|"
    Table[5][7] = "x"
    outputtable(Table)
    return Table,player,Winner,Gameend,robot

def outputtable(Table):
    print("y")
    print("")
    for i in range(8):
        for j in range(8):
            print(Table[i][j],end="")
        print("")

def inputtotable(Table,player):
    print("Player",player,"turn")
    Input = str(input("Input your coordinates for your turn in the format 'x,y': "))
    Valid = False
    Valid = Validation(Table,Input)
    while Valid == False:
        Input = str(input("Input your coordinates for your turn in the format 'x,y': "))        
        Valid = Validation(Table,Input)
    if Input == "1,1":
        Table[4][1] = player
    if Input == "1,2":
        Table[2][1] = player
    if Input == "1,3":
        Table[0][1] = player
    if Input == "2,1":
        Table[4][3] = player
    if Input == "2,2":
        Table[2][3] = player
    if Input == "2,3":
        Table[0][3] = player
    if Input == "3,1":
        Table[4][5] = player
    if Input == "3,2":
        Table[2][5] = player
    if Input == "3,3":
        Table[0][5] = player
    return Table

def wincondition(Table,player,Gameend,Winner,robot):
    if Table[0][1] == player and Table[0][3] == player and Table[0][5] == player:
        Winner = True
        Gameend = True
    if Table[2][1] == player and Table[2][3] == player and Table[2][5] == player:
        Winner = True
        Gameend = True
    if Table[4][1] == player and Table[4][3] == player and Table[4][5] == player:
        Winner = True
        Gameend = True
    if Table[0][1] == player and Table[2][1] == player and Table[4][1] == player:
        Winner = True
        Gameend = True
    if Table[0][3] == player and Table[2][3] == player and Table[4][3] == player:
        Winner = True
        Gameend = True
    if Table[0][5] == player and Table[2][5] == player and Table[4][5] == player:
        Winner = True
        Gameend = True
    if Table[4][5] == player and Table[2][3] == player and Table[0][1] == player:
        Winner = True
        Gameend = True
    if Table[4][1] == player and Table[2][3] == player and Table[0][5] == player:
        Winner = True
        Gameend = True
    if Table[0][1] == robot and Table[0][3] == robot and Table[0][5] == robot:
        Winner = True
        Gameend = True
    if Table[2][1] == robot and Table[2][3] == robot and Table[2][5] == robot:
        Winner = True
        Gameend = True
    if Table[4][1] == robot and Table[4][3] == robot and Table[4][5] == robot:
        Winner = True
        Gameend = True
    if Table[0][1] == robot and Table[2][1] == robot and Table[4][1] == robot:
        Winner = True
        Gameend = True
    if Table[0][3] == robot and Table[2][3] == robot and Table[4][3] == robot:
        Winner = True
        Gameend = True
    if Table[0][5] == robot and Table[2][5] == robot and Table[4][5] == robot:
        Winner = True
        Gameend = True
    if Table[4][5] == robot and Table[2][3] == robot and Table[0][1] == robot:
        Winner = True
        Gameend = True
    if Table[4][1] == robot and Table[2][3] == robot and Table[0][5] == robot:
        Winner = True
        Gameend = True
    return Winner,Gameend

def tie(Table,Winner,Gameend):
    if Winner == False and Table[0][1] != " " and Table[0][3] != " " and Table[0][5] != " " and Table[2][1] != " " and Table[2][3] != " " and Table[2][5] != " " and Table[4][1] != " " and Table[4][3] != " " and Table[4][5] != " ":
        Gameend = True
    return Gameend

def Validation(Table,Input):
    if len(Input) != 3:
        Valid = False
    else:
        if ord(Input[0:1]) > 51 or ord(Input[0:1]) < 49:
            Valid = False
        else:            
            if int(Input[0:1]) > 3 or int(Input[0:1]) < 1:
                Valid = False
            else:
                if Input[1:2] != ",":
                    Valid = False
                else:
                    if ord(Input[2:3]) > 51 or ord(Input[2:3]) < 49:
                        Valid = False
                    else:
                        if int(Input[2:3]) > 3 or int(Input[2:3]) < 1:
                            Valid = False
                        else:
                            Valid = True
    if Valid == True:
        if Input == "1,1" and Table[4][1] != " ":
            Valid = False
        if Input == "1,2" and Table[2][1] != " ":
            Valid = False
        if Input == "1,3" and Table[0][1] != " ":
            Valid = False
        if Input == "2,1" and Table[4][3] != " ":
            Valid = False
        if Input == "2,2" and Table[2][3] != " ":
            Valid = False
        if Input == "2,3" and Table[0][3] != " ":
            Valid = False
        if Input == "3,1" and Table[4][5] != " ":
            Valid = False
        if Input == "3,2" and Table[2][5] != " ":
            Valid = False
        if Input == "3,3" and Table[0][5] != " ":
            Valid = False
    return Valid

def playerturn(Table,player,Winner,Gameend,robot):
    Table = inputtotable(Table,player)
    outputtable(Table)
    Winner,Gameend = wincondition(Table,player,Gameend,Winner,robot)
    Gameend = tie(Table,Winner,Gameend)
    return Table,Winner,Gameend

def robotturn(Table,robot,player,Gameend,Winner,count):
    Table = robotinput(Table,robot,count,player)
    outputtable(Table)
    Winner,Gameend = wincondition(Table,player,Gameend,Winner,robot)
    Gameend = tie(Table,Winner,Gameend)
    return Table,Winner,Gameend

def robotinput(Table,robot,count,player):
    Played = False
    if count == 0:
        X = random.randint(1,5)
        if X == 1:
            Table[0][1] = "X"
        if X == 2:
            Table[0][5] = "X"
        if X == 3:
            Table[4][5] = "X"
        if X == 4:
            Table[4][1] = "X"
        if X == 5:
            Table[2][3] = "X"
    if count == 1:
        if Table[2][3] != " ":
            X = random.randint(1,4)
            if X == 1:
                Table[0][1] = "O"
            if X == 2:
                Table[0][5] = "O"
            if X == 3:
                Table[4][5] = "O"
            if X == 4:
                Table[4][1] = "O"
        else:
            Table[2][3] = "O"
    if count == 2:
        if Table[0][1] == "X" and Table[0][3] == "O":
            Table[2][3] = "X"
            Played = True
        if Table[0][5] == "X" and Table[0][3] == "O":
            Table[2][3] = "X"
            Played = True
        if Table[0][5] == "X" and Table[2][5] == "O":
            Table[2][3] = "X"
            Played = True
        if Table[4][5] == "X" and Table[2][5] == "O":
            Table[2][3] = "X"
            Played = True
        if Table[4][5] == "X" and Table[4][3] == "O":
            Table[2][3] = "X"
            Played = True
        if Table[4][1] == "X" and Table[4][3] == "O":
            Table[2][3] = "X"
            Played = True
        if Table[4][1] == "X" and Table[2][1] == "O":
            Table[2][3] = "X"
            Played = True
        if Table[0][1] == "X" and Table[2][1] == "O":
            Table[2][3] = "X"
            Played = True
        if Played == False:
            X = random.randint(1,2)
            if X == 1:
                if Table[2][3] == " " and Played == False:
                    Table[2][3] = "X"
                    Played = True
            else:
                if Table[2][3] == "X" and Table[0][3] == "O" or Table[4][3] == "O" or Table[2][1] == "O" or Table[2][5] == "O" and Played == False:
                    X = random.randint(1,4)
                    if X == 1:
                        Table[0][1] = "X"
                    if X == 2:
                        Table[0][5] = "X"
                    if X == 3:
                        Table[4][5] = "X"
                    if X == 4:
                        Table[4][1] = "X"
                    Played = True
            if Table[2][3] == "O" and Played == False:
                X = random.randint(1,3)
                if Table[0][1] == "X" and Played == False:
                    if X == 1:
                        Table[0][5] = "X"
                    if X == 2:
                        Table[4][5] = "X"
                    if X == 3:
                        Table[4][1] = "X"
                    Played = True
                if Table[0][5] == "X" and Played == False:
                    if X == 1:
                        Table[0][1] = "X"
                    if X == 2:
                        Table[4][5] = "X"
                    if X == 3:
                        Table[4][1] = "X"
                    Played = True
                if Table[4][1] == "X" and Played == False:
                    if X == 1:
                        Table[0][5] = "X"
                    if X == 2:
                        Table[4][5] = "X"
                    if X == 3:
                        Table[0][1] = "X"
                    Played = True
                if Table[4][5] == "X" and Played == False:
                    if X == 1:
                        Table[0][5] = "X"
                    if X == 2:
                        Table[0][1] = "X"
                    if X == 3:
                        Table[4][1] = "X"
                    Played = True
            if Played == False:
                Table = RNG(Table,robot,Played)
    if count == 3:
        Played = False
        if Table[0][1] == "X" and Table[4][5] == "X" or Table[0][5] == "X" and Table[4][1] == "X":
            X = random.randint(1,4)
            if X == 1:
                Table[2][1] = "O"
            if X == 2:
                Table[2][5] = "O"
            if X == 3:
                Table[0][3] = "O"
            if X == 4:
                Table[4][3] = "O"
            Played = True
        else:
            if Table[0][1] == "X" and Table[2][5] == "X":
                Table[0][5] = "O"
                Played = True
            if Table[0][1] == "X" and Table[4][3] == "X":
                Table[4][1] = "O"
                Played = True
            if Table[0][5] == "X" and Table[4][3] == "X":
                Table[4][5] = "O"
                Played = True
            if Table[0][5] == "X" and Table[2][1] == "X":
                Table[0][1] = "O"
                Played = True
            if Table[4][5] == "X" and Table[2][1] == "X":
                Table[4][1] = "O"
                Played = True
            if Table[4][5] == "X" and Table[0][3] == "X":
                Table[0][5] = "O"
                Played = True
            if Table[4][1] == "X" and Table[2][5] == "X":
                Table[4][5] = "O"
                Played = True
            if Table[4][1] == "X" and Table[0][3] == "X":
                Table[0][1] = "O"
                Played = True
        if Table[0][1] == "X" and Table[2][3] == "X" and Table[4][5] == "O":
            X = random.randint(1,2)
            if X == 1:
                Table[4][1] = "O"
            if X == 2:
                Table[0][5] = "O"
            Played = True
        if Table[4][5] == "X" and Table[2][3] == "X" and Table[0][1] == "O":
            X = random.randint(1,2)
            if X == 1:
                Table[4][1] = "O"
            if X == 2:
                Table[0][5] = "O"
            Played = True
        if Table[4][1] == "X" and Table[2][3] == "X" and Table[0][5] == "O":
            X = random.randint(1,2)
            if X == 1:
                Table[4][5] = "O"
            if X == 2:
                Table[0][1] = "O"
            Played = True
        if Table[0][5] == "X" and Table[2][3] == "X" and Table[4][1] == "O":
            X = random.randint(1,2)
            if X == 1:
                Table[4][5] = "O"
            if X == 2:
                Table[0][1] = "O"
            Played = True
        if Table[0][3] == "X" and Table[2][1] == "X":
            X = random.randint(1,3)
            if X == 1:
                Table[4][1] = "O"
            if X == 2:
                Table[0][5] = "O"
            if X == 3:
                Table[0][1] = "O"
            Played = True
        if Table[4][3] == "X" and Table[2][1] == "X":
            X = random.randint(1,3)
            if X == 1:
                Table[4][1] = "O"
            if X == 2:
                Table[4][5] = "O"
            if X == 3:
                Table[0][1] = "O"
            Played = True
        if Table[4][3] == "X" and Table[2][5] == "X":
            X = random.randint(1,3)
            if X == 1:
                Table[4][1] = "O"
            if X == 2:
                Table[0][5] = "O"
            if X == 3:
                Table[4][5] = "O"
            Played = True
        if Table[0][3] == "X" and Table[2][5] == "X":
            X = random.randint(1,3)
            if X == 1:
                Table[4][5] = "O"
            if X == 2:
                Table[0][5] = "O"
            if X == 3:
                Table[0][1] = "O"
            Played = True
        if Played == False:
            Table,Played = blockmechanics(Table,player,Played,robot)
            if Played == False:
                Table = RNG(Table,robot,Played)
    if count == 4:
        Played = False
        Table,Played = simplewincondition(Table,robot,Played)
        if Played == False:
            Table,Played = blockmechanics(Table,player,Played,robot)
        if Played == False:
            if Table[0][1] == "X" and Table[0][3] == "O" and Table[2][1] == " ":
                Table[2][1] = "X"
                Played = True
            if Table[0][1] == "X" and Table[2][1] == "O" and Table[0][3] == " ":
                Table[0][3] = "X"
                Played = True
            if Table[0][5] == "X" and Table[0][3] == "O" and Table[2][5] == " ":
                Table[2][5] = "X"
                Played = True
            if Table[0][5] == "X" and Table[2][5] == "O" and Table[0][3] == " ":
                Table[0][3] = "X"
                Played = True
            if Table[4][5] == "X" and Table[2][5] == "O" and Table[4][3] == " ":
                Table[4][3] = "X"
                Played = True
            if Table[4][5] == "X" and Table[4][3] == "O" and Table[2][5] == " ":
                Table[2][5] = "X"
                Played = True
            if Table[4][1] == "X" and Table[4][3] == "O" and Table[2][1] == " ":
                Table[2][1] = "X"
                Played = True
            if Table[4][1] == "X" and Table[2][1] == "O" and Table[4][3] == " ":
                Table[4][3] = "X"
                Played = True
        if Played == False:
            if Table[2][1] == "O" and Table[0][5] == "O" and Table[0][1] == " ":
                Table[0][1] = "X"
                Played = True
            if Table[2][1] == "O" and Table[4][5] == "O" and Table[4][1] == " ":
                Table[4][1] = "X"
                Played = True
            if Table[0][3] == "O" and Table[4][5] == "O" and Table[0][5] == " ":
                Table[0][5] = "X"
                Played = True
            if Table[0][3] == "O" and Table[4][1] == "O" and Table[0][1] == " ":
                Table[0][1] = "X"
                Played = True
            if Table[2][5] == "O" and Table[4][1] == "O" and Table[4][5] == " ":
                Table[4][5] = "X"
                Played = True
            if Table[2][5] == "O" and Table[0][1] == "O" and Table[0][5] == " ":
                Table[0][5] = "X"
                Played = True
            if Table[4][3] == "O" and Table[0][5] == "O" and Table[4][5] == " ":
                Table[4][5] = "X"
                Played = True
            if Table[4][3] == "O" and Table[0][1] == "O" and Table[4][1] == " ":
                Table[4][1] = "X"
                Played = True
        if Played == False:
            Table = RNG(Table,robot,Played)
    if count == 5:
        Played = False
        Table,Played = simplewincondition(Table,robot,Played)
        if Played == False:
            Table,Played = blockmechanics(Table,player,Played,robot)
        if Played == False:
            Table = RNG(Table,robot,Played)
    if count == 6:
        Played = False
        Table,Played = simplewincondition(Table,robot,Played)
        if Played == False:
            Table,Played = blockmechanics(Table,player,Played,robot)
        if Played == False:
            Table = RNG(Table,robot,Played)
    if count == 7:
        Played = False
        Table,Played = simplewincondition(Table,robot,Played)
        if Played == False:
            Table,Played = blockmechanics(Table,player,Played,robot)
        if Played == False:
            Table = RNG(Table,robot,Played)
    if count == 8:
        Played = False
        Table,Played = simplewincondition(Table,robot,Played)
        if Played == False:
            Table,Played = blockmechanics(Table,player,Played,robot)
        if Played == False:
            Table = RNG(Table,robot,Played)
    return Table

def RNG(Table,robot,Played):
    while Played == False:        
        X = random.randint(1,9)
        if X == 1 and Table[0][1] == " ":
            Table[0][1] = robot
            Played = True
        if X == 2 and Table[0][3] == " ":
            Table[0][3] = robot
            Played = True
        if X == 3 and Table[0][5] == " ":
            Table[0][5] = robot
            Played = True
        if X == 4 and Table[2][1] == " ":
            Table[2][1] = robot
            Played = True
        if X == 5 and Table[2][3] == " ":
            Table[2][3] = robot
            Played = True
        if X == 6 and Table[2][5] == " ":
            Table[2][5] = robot
            Played = True
        if X == 7 and Table[4][1] == " ":
            Table[4][1] = robot
            Played = True
        if X == 8 and Table[4][3] == " ":
            Table[4][3] = robot
            Played = True
        if X == 9 and Table[4][5] == " ":
            Table[4][5] = robot
            Played = True
    return Table
            
def blockmechanics(Table,player,Played,robot):
    for i in range(0,6,2):
        if Table[i][1] == player and Table[i][3] == player and Played == False and Table[i][5] == " ":
            Table[i][5] = robot
            Played = True
        if Table[i][3] == player and Table[i][5] == player and Played == False and Table[i][1] == " ":
            Table[i][1] = robot
            Played = True
        if Table[i][5] == player and Table[i][1] == player and Played == False and Table[i][3] == " ":
            Table[i][3] = robot
            Played = True
    for i in range(1,7,2):
        if Table[0][i] == player and Table[2][i] == player and Played == False and Table[4][i] == " ":
            Table[4][i] = robot
            Played = True
        if Table[4][i] == player and Table[2][i] == player and Played == False and Table[0][i] == " ":
            Table[0][i] = robot
            Played = True
        if Table[0][i] == player and Table[4][i] == player and Played == False and Table[2][i] == " ":
            Table[2][i] = robot
            Played = True
    if Played == False:
        if Table[0][1] == player and Table[2][3] == player and Table[4][5] == " ":
            Table[4][5] = robot
            Played = True
    if Played == False:
        if Table[4][5] == player and Table[2][3] == player and Table[0][1] == " ":
            Table[0][1] = robot
            Played = True
    if Played == False:
        if Table[0][1] == player and Table[4][5] == player and Table[2][3] == " ":
            Table[2][3] = robot
            Played = True
    if Played == False:
        if Table[0][5] == player and Table[2][3] == player and Table[4][1] == " ":
            Table[4][1] = robot
            Played = True
    if Played == False:
        if Table[4][1] == player and Table[2][3] == player and Table[0][5] == " ":
            Table[0][5] = robot
            Played = True
    if Played == False:
        if Table[0][5] == player and Table[4][1] == player and Table[2][3] == " ":
            Table[2][3] = robot
            Played = True
    return Table,Played
    
def simplewincondition(Table,robot,Played):
    for i in range(0,6,2):
        if Table[i][1] == robot and Table[i][3] == robot and Played == False and Table[i][5] == " ":
            Table[i][5] = robot
            Played = True
        if Table[i][3] == robot and Table[i][5] == robot and Played == False and Table[i][1] == " ":
            Table[i][1] = robot
            Played = True
        if Table[i][5] == robot and Table[i][1] == robot and Played == False and Table[i][3] == " ":
            Table[i][3] = robot
            Played = True
    for i in range(1,7,2):
        if Table[0][i] == robot and Table[2][i] == robot and Played == False and Table[4][i] == " ":
            Table[4][i] = robot
            Played = True
        if Table[4][i] == robot and Table[2][i] == robot and Played == False and Table[0][i] == " ":
            Table[0][i] = robot
            Played = True
        if Table[0][i] == robot and Table[4][i] == robot and Played == False and Table[2][i] == " ":
            Table[2][i] = robot
            Played = True
    if Played == False:
        if Table[0][1] == robot and Table[2][3] == robot and Table[4][5] == " ":
            Table[4][5] = robot
            Played = True
    if Played == False:
        if Table[4][5] == robot and Table[2][3] == robot and Table[0][1] == " ":
            Table[0][1] = robot
            Played = True
    if Played == False:
        if Table[0][1] == robot and Table[4][5] == robot and Table[2][3] == " ":
            Table[2][3] = robot
            Played = True
    if Played == False:
        if Table[0][5] == robot and Table[2][3] == robot and Table[4][1] == " ":
            Table[4][1] = robot
            Played = True
    if Played == False:
        if Table[4][1] == robot and Table[2][3] == robot and Table[0][5] == " ":
            Table[0][5] = robot
            Played = True
    if Played == False:
        if Table[0][5] == robot and Table[4][1] == robot and Table[2][3] == " ":
            Table[2][3] = robot
            Played = True
    return Table,Played
    
def game():
    Table,player,Winner,Gameend,robot = Setuptable()
    count = 0
    while Gameend == False:
        if player == "X":
            Table,Winner,Gameend = playerturn(Table,player,Winner,Gameend,robot)
            count = count + 1
            if Gameend == False:
                Table,Winner,Gameend = robotturn(Table,robot,player,Gameend,Winner,count)
                count = count + 1
                if Winner == True:
                    print("The AI beat you")
            else:
                if Winner == True:
                    print("You won the unbeatable AI")
                else:
                    print("It was a tie :/")
        else:
            Table,Winner,Gameend = robotturn(Table,robot,player,Gameend,Winner,count)
            count = count + 1
            if Gameend == False:
                Table,Winner,Gameend = playerturn(Table,player,Winner,Gameend,robot)
                count = count + 1
                if Winner == True:
                    print("You won the unbeatable AI")
            else:
                if Winner == True:
                    print("The AI beat you")
                else:
                    print("It was a tie :/")
    Input = str(input("if you want to play again input exactly 'yes': "))
    if Input == "yes":
        game()
    else:
        print("Have a wonderful day!")

game()
