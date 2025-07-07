def Setuptable():
    Winner = False
    Gameend = False
    Table = [[" " for i in range(8)] for j in range(8)]
    player = "X"
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
    return Table,player,Winner,Gameend

def outputtable(Table):
    print("y")
    print("")
    for i in range(8):
        for j in range(8):
            print(Table[i][j],end="")
        print("")

def swapplayers(player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player

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

def wincondition(Table,player,Gameend,Winner):
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

def game():    
    Table,player,Winner,Gameend = Setuptable()
    while Gameend == False:
        Table = inputtotable(Table,player)
        outputtable(Table)
        Winner,Gameend = wincondition(Table,player,Gameend,Winner)
        Gameend = tie(Table,Winner,Gameend)
        if Gameend == True:
            if Winner == True:
                print("Player",player,"has won, congratulations!")
            else:
                print("It was a tie :/")
        else:
            player = swapplayers(player)
    Input = str(input("if you want to play again input exactly 'yes': "))
    if Input == "yes":
        game()
    else:
        print("Have a wonderful day!")

game()
