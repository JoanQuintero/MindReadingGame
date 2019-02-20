from math import *

def MindGame():
    #MIND READING GAME
    # This Program has been designed for TWO Players.
    # Program will first ask who wants to be the Mind Reader,
    # and who wants to be the Mind Readee(The one whose mind is being read)

    print(" ")
    print(" ")

    #########################################################
    #########################################################
    ###############        INSTRUCTIONS       ###############
    #########################################################
    #########################################################
    print(" ")
    print(" ")
    print("       "," DO YOU HAVE WHAT IT TAKES TO PLAY A MIND GAME?")
    print("After choosing a number below, each players position will be described")
    print(" ")
    print("                  ","⌛ TYPE 1 FOR MIND READER ⌛")
    print("                  ","⌛ TYPE 2 FOR MIND READEE ⌛")
    print(" ")

    #########################################################
    #########################################################
    ################ This has been created ##################
    ###############    To refer to end of     ###############
    ###############        instructions.  ###################
    #########################################################
    #########################################################
    m = ("Mind Reader")
    m2 = ("Mind Readee")
    #########################################################
    #########################################################
    ################ This has been created ##################
    ###############    To refer to PLAYERS    ###############
    ###############        assignment.    ###################
    #########################################################
    #########################################################
    print(" ")


    N1  =    eval(input("                 Which Player Will You Be? Player:  "))

    if N1 == 1:
        print(" ")
        print(" ")
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
    #############
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("        --------------------------------------------------")
    ############# 
        print("                        ◐  Second Player  ◐  ")
        print("        --------------------------------------------------")
        print(" ")
        print("              ◐ You've been assigned: " , m2, "◐")
        print("                                 ⬇                       ")
        print(" ")
    #############   
        print("           ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻ ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻  ")
        print("          Carefully read and remember your instructions  ")
        print("                         ⦕  MIND READEE ⦖          ")
        print("               ☾TASK☽ - Input a number from 1 to N")
        print("           ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻ ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻  ")
        print(" ")
        print(" ")
     #############
        print("    ----------------------------------------------------------")
        print(" ")
        print(" ")
              
    if N1 == 2:
        print("  ")
        print("  ")
    #############
        print("        --------------------------------------------------")
    ############# 
        print("                        ◐  Second Player  ◐  ")
        print("        --------------------------------------------------")
        print(" ")
        print("              ◐ You've been assigned: " , m2, "◐")
        print("                                 ⬇                       ")
        print(" ")
    #############   
        print("           ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻ ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻  ")
        print("          Carefully read and remember your instructions  ")
        print("                         ⦕  MIND READEE ⦖          ")
        print("               ☾TASK☽ - Input a number from 1 to N")
        print("           ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻ ⎺ ⎻ ⎼ ⎽ ⎼ ⎻ ⎺ ⎻ ⎼ ⎼ ⎻  ")
    #############          
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
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
    #############
        print(" ")
        print(" ")
     #############
        print("    ----------------------------------------------------------")
        print(" ")
        print(" ")

    #########################################################
    #########################################################
    ################ This has been created ##################
    ############### to separate if statements ###############
    ###############     from one another. ###################
    #########################################################
    #########################################################



    StartKey = 0
    while ((N1 == 1 or N1 == 2) and StartKey != 3) :
        StartKey = eval(input("                        Type 3 to START " ))


    if (N1 != 1 and N1 != 2 or StartKey != 3):
        print(" ")
        print("The option to type: " ,  N1," was not provided")
        print("⚫ You cannot play against ṯℎę ċōṁṗüṯęɍ ⚫")
        print(" ")
        print("                ¯_(ツ)_/¯")
        print(" ")


    if (N1 == 1 and StartKey == 3):
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨ GAME ON ! ⌨⌨⌨⌨⌨⌨⌨⌨")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨")
        print(" ")
        print("            ","While playing Type 0 on any questions ")
        print("                    to 'PAUSE' or 'END' game")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ", m + ", choose the AMOUNT of TURNS. ex. 100: would be 100 turns each")
        print(" ")
        print(" ")
        AmountOfGamesToPlay = eval(input("Choose the amount of turns: "))
        print(" ")
        print(" ")
        print("The amount of turns is set to",AmountOfGamesToPlay,"")
        print(" Game ends at 0 turns left.")
        print(" ")
        print(" ")
        print(" ")
        
    if (N1 == 2 and StartKey == 3):
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨ GAME ON ! ⌨⌨⌨⌨⌨⌨⌨⌨")
        print("          ⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨⌨")
        print(" ")
        print("            ","While playing Type 0 on any questions ")
        print("                    to 'PAUSE' or 'END' game")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ", m2 + ", choose the AMOUNT of TURNS. ex. 100: would be 100 turns each")
        print(" ")
        print(" ")
        AmountOfGamesToPlay = eval(input("Choose the amount of turns: "))
        print(" ")
        print(" ")
        print("The amount of turns is set to",AmountOfGamesToPlay,"")
        print(" Game ends at 0 turns left.")
        print(" ")
        print(" ")
        print(" ")
        
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
        Fatal = 1
        i = 0


    # Game loop: Keep it going till game is over
        while i < (AmountOfGamesToPlay): # Condition for continuing
            
            
        # switches players
            if currentPlayer == "Mind Readee" and AmountOfGamesToPlay != 0:
                count_PlayerOneTurns += 1
                print("Mind Readee input # " + str(count_PlayerOneTurns))
                ask = "Player " + currentPlayer + " what is your input: "
                currentInput = input(ask)
                OneInput = int(OneInput) + int(currentInput)
                currentPlayer = "Mind Reader"

                for x in range(40):
                    print()
                
                
            if currentPlayer == "Mind Reader" and AmountOfGamesToPlay != 0:
                count_PlayerTwoTurns += 1
                print("Mind Reader turn #" + str(count_PlayerTwoTurns))
                asking = "Player " + currentPlayer + " what is your guess: "
                currentInpuT = input(asking)
                TwoInput = int(TwoInput) + int(currentInpuT)
                currentPlayer = "Mind Readee"
                AmountOfGamesToPlay -= 1
            
                for x in range(19):
                    print()
                    
                
                print("Amount of turns left for each player: ", AmountOfGamesToPlay)
                
                for x in range(20):
                    print()
                
            if (currentInput == currentInpuT):
                Rightcount = Rightcount + 1
                


            if AmountOfGamesToPlay == 0:
                Total_runs = count_PlayerTwoTurns
                Fatal -= 1
                print("Game Over - " + str(Fatal) + " Games left. ")
                print(" ")
                # Formula for percentage:
                Percentage = (100 * Rightcount)
                Percentage = Percentage / Total_runs
                print("Total games played per player: ", str(Total_runs) + " games")
                print(" ")
                print("Mind Reader has " + str(Rightcount) + " right answers")
                print("Percentage of Mind Reader Right Answers: ", str(Percentage) + "%")
                
                

                

         
MindGame()



    #Restart/End
                
    # Formula

    # Percentage = (Amount * 100)/Total






