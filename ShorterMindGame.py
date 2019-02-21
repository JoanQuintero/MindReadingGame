from math import *
 
 
m = ("Mind Reader")
m2 = ("Mind Readee")
GamesLeft = 1
     
def printPlayer1(m):
     
    print("        --------------------------------------------------")
    print("                        ◐  First Player  ◐")
    print("        --------------------------------------------------")
    print(" ")
    print("              ◐ You've been assigned: " ,   m, "◐")
    print("                                ⬇                       ")
    print(" ")
    print("           ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻ ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻  ")
    print("          Carefully read and remember your instructions  ")
    print("                         ⦕  MIND READER ⦖          ")
    print("               ☾TASK☽ - Guess opponents inputs      ")
    print("           ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻ ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻  ")
 
def printPlayer2(m2):
     
    print("        --------------------------------------------------")
    print("                        ◐  Second Player  ◐  ")
    print("        --------------------------------------------------")
    print(" ")
    print("              ◐ You've been assigned: " , m2, "◐")
    print("                                 ⬇                       ")
    print(" ")
    print("           ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻ ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻  ")
    print("          Carefully read and remember your instructions  ")
    print("                         ⦕  MIND READEE ⦖          ")
    print("               ☾TASK☽ - Input a number from 1 to N")
    print("           ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻ ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻  ")
    print("\n\n")
    print("    ----------------------------------------------------------")
 
def printResults(GamesLeft, count_PlayerTwoTurns, Rightcount):
     
    Total_runs = count_PlayerTwoTurns
    GamesLeft -= 1
    print("Game Over - " + str(GamesLeft) + " Games left. ")
    print(" ")
    # Formula for percentage:
    Percentage = (100 * Rightcount)
    Percentage = Percentage / Total_runs
    print("Total games played per player: ", str(Total_runs) + " games")
    print(" ")
    print("Mind Reader has " + str(Rightcount) + " right answers")
    print("Percentage of Mind Reader Right Answers: ", str(Percentage) + "%")
                 
def SpaceLoop(n):
# This function is for spaces bigger than 3 lines to avoid typing to many \n !!
    for x in range(n):
        print()
 
def ErrorMsg(N1):
        print("The option to type: " ,  N1," was not provided")
        print("⚫ You cannot play against ṯℎę ċōṁṗüṯęɍ ⚫")
        print(" ")
        print("                ¯_(ツ)_/¯")
         
def MindGame():
 
    SpaceLoop(4)
    print("       "," DO YOU HAVE WHAT IT TAKES TO PLAY A MIND GAME?")
    print("After choosing a number below, each players position will be described")
    print(" ")
    print("                  ","⌛ TYPE 1 FOR MIND READER ⌛")
    print("                  ","⌛ TYPE 2 FOR MIND READEE ⌛")
    print("\n\n")
 
    N1  =    eval(input("                 Which Player Will You Be? Player:  "))
 
    if N1 == 1:
        print("\n\n")
        printPlayer1(m)
        SpaceLoop(5)
        printPlayer2(m2)
        print("\n\n")
               
    if N1 == 2:
        print("\n\n")
        printPlayer2(m2)         
        SpaceLoop(5)
        printPlayer1(m)
        print("\n\n")
 
 
    StartKey = 0
    while ((N1 == 1 or N1 == 2) and StartKey != 3) :
        StartKey = eval(input("                        Type 3 to START " ))
 
 
    if (N1 != 1 and N1 != 2 or StartKey != 3):
        print("\n\n")
        ErrorMsg(N1)
        print("\n\n")
 
    if (N1 == 1 and StartKey == 3):
        SpaceLoop(5)
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨ GAME ON ! ⌨⌨⌨⌨⌨⌨⌨⌨")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨")
        print("\n\n")
        print(" ", m + " Chooses the range for the game, \n example: 10 would be from 1 to 10 only.")
        print(" ")
        Range = eval(input(" Choose the range: "))
        print("\n\n")
        print(" ", m + ", now choose the AMOUNT of TURNS. ex. 100: would be 100 turns each")
        print("\n\n\n")
        AmountOfGamesToPlay = eval(input("Choose the amount of turns: "))
        print("\n\n\n")
        print("The range of the game is set to",Range,"")
        print("The amount of turns is set to",AmountOfGamesToPlay,"")
        print(" Game ends at 0 turns left.")
        print("\n\n\n")
         
    if (N1 == 2 and StartKey == 3):
        SpaceLoop(5)
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨ GAME ON ! ⌨⌨⌨⌨⌨⌨⌨⌨")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨")
        print("\n\n")
        print(" ", m2 + " Chooses the range for the game, \n example: 10 would be from 1 to 10 only.")
        print(" ")
        Range = eval(input(" Choose the range: "))
        print("\n\n")
        print(" ", m2 + ", now choose the AMOUNT of TURNS. ex. 100: would be 100 turns each")
        print("\n\n\n")
        AmountOfGamesToPlay = eval(input("Choose the amount of turns: "))
        print("\n\n\n")
        print("The range of the game is set to",Range,"")
        print("The amount of turns is set to",AmountOfGamesToPlay,"")
        print(" Game ends at 0 turns left.")
        print("\n\n\n")
         
    if AmountOfGamesToPlay > 0:
 
        currentPlayer = "Mind Readee"
        count_PlayerOneTurns = 0
        count_PlayerTwoTurns = 0
        OneInput = 0
        TwoInput = 0
        currentInput = 0
        Rightcount = 0
        currentInpuT = 1
        Total_runs = 0
        GoodInput = 0
       
 
    # Game Loop
        while 0 < (AmountOfGamesToPlay): 
             
             
        # Player Switch
            if currentPlayer == "Mind Readee" and AmountOfGamesToPlay != 0:
                count_PlayerOneTurns += 1
                print("Mind Readee input # " + str(count_PlayerOneTurns))
                ask = "Player " + currentPlayer + " what is your input: "
                currentInput = input(ask)
                OneInput = int(OneInput) + int(currentInput)
                currentPlayer = "Mind Reader"
                 
                while int(currentInput) > int(Range) or int(currentInput) < 0:
                    print("\n The option to type",currentInput, " was not provided.\n\n Try again...")
                    currentInput = input(ask)
 
                SpaceLoop(40)
                 
            if currentPlayer == "Mind Reader" and AmountOfGamesToPlay != 0:
                count_PlayerTwoTurns += 1
                print("Mind Reader turn #" + str(count_PlayerTwoTurns))
                asking = "Player " + currentPlayer + " what is your guess: "
                currentInpuT = input(asking)
                TwoInput = int(TwoInput) + int(currentInpuT)
                currentPlayer = "Mind Readee"
                AmountOfGamesToPlay -= 1
                 
                while int(currentInpuT) > int(Range) or int(currentInpuT) < 0:
                    print("\n The option to type",currentInpuT, " was not provided.\n\n Try again...")
                    currentInpuT = input(asking)
             
                SpaceLoop(19)
                     
                print("Amount of turns left for each player: ", AmountOfGamesToPlay)
                 
                SpaceLoop(20)
                 
            if (currentInput == currentInpuT):
                Rightcount = Rightcount + 1
                 
 
 
        # Done looping
 
        printResults(GamesLeft, count_PlayerTwoTurns, Rightcount)
                 
 
                 
 
          
MindGame()
