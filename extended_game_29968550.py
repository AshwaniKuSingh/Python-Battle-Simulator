""""                  *-*-*Overview*-*-*
This program consist of five function
1. option() function display the list if units available to the user.
2. appendUnitsToArmyOne() function for appending units to the army of player-1.
3. appendUnitsToArmyTwo() function for appending units to the army of player-2.
4. Medics() function inside combat() function to pop the died unit and append it to the end of their respective list
   until medics value is not zero and reduce the medics value by one.
5. combat(armyOneList,armyTwoList) function to begin the fight between player one and player two units.
"""
armyOneList = list()
armyTwoList = list()
armyOneRemainingFunds = 0
armyTwoRemainingFunds = 0
"""
option() function to render the available units to user.
"""
def option() :
    print("1. Archer = $2")
    print("2. Soldier = $1")
    print("3. Knight = $2")
    print("4. Siege Equipment = $2")
    print("5. Wizard = $3")
"""
appendUnitsToArmyOne() function to append units to army of player-1 and this function update the unused fund value
to armyOneRemaainingFunds which is a global variable. Later this remaining funds will be used as medics for player=1.
"""
def appendUnitsToArmyOne():
    global armyOneRemainingFunds
    playerOneFunds=10
    # The while loop will break in only two cases
    # First if user used all the fund values. Second if user types "n" for no addition of unit.
    while playerOneFunds >= 1:
        p=input("If u want to add unit hit y or n not to add =")
        if(p=="y"):
            option()
            r = input("Your Selection =")
            if r == "1":
                if (playerOneFunds >= 2):
                    armyOneList.append("Archer")
                    playerOneFunds = playerOneFunds - 2
                    print("Your remaining funds is = $" + str(playerOneFunds))
                else:
                    print("You dont't have sufficient fund to buy this unit")
            elif r == "2":
                if (playerOneFunds >= 1):
                    armyOneList.append("Soldier")
                    playerOneFunds = playerOneFunds - 1
                    print("Your remaining funds is = $" + str(playerOneFunds))
                else:
                    print("You dont't have sufficient fund to buy this unit")
            elif r == "3":
                if (playerOneFunds >= 2):
                    armyOneList.append("Knight")
                    playerOneFunds = playerOneFunds - 2
                    print("Your remaining funds is = $" + str(playerOneFunds))
                else:
                    print("You dont't have sufficient fund to buy this unit")
            elif r=="4" :
                if(playerOneFunds >= 2) :
                    armyOneList.append("Siege Equipment")
                    playerOneFunds = playerOneFunds - 2
                    print("Your remaining funds is = $" + str(playerOneFunds))
                else :
                    print("You dont't have sufficient fund to buy this unit")
            elif r=="5" :
                if (playerOneFunds >= 3):
                    armyOneList.append("Wizard")
                    playerOneFunds = playerOneFunds - 3
                    print("Your remaining funds is = $" + str(playerOneFunds))
                else:
                    print("You dont't have sufficient fund to buy this unit")
            # If user input anything other than 1,2,3, you selected wrong input message will be rendered
            else :
                print("You selected wrong option")
        # If user hits "n", the loop will break and user will no longer be able to append unit
        elif p=="n" :
            break
        # Else if user types anything other than "y" or "n",Invalid selection message will be rendered.
        else :
            print("Invalid Selection")
    print("Player one your army units list is = " + str(armyOneList))
    armyOneRemainingFunds = playerOneFunds
    print("Your remaining fund is = $" + str(armyOneRemainingFunds))
    print("\n")
"""
appendUnitsToArmyTwo() function to append the units to army of player-2 and this function update the unused fund value
to armyTwoRemaainingFunds global variable. Later this remaining funds will be used as medics.
"""
def appendUnitsToArmyTwo():
    global armyTwoRemainingFunds
    playerTwoFunds=10
    # The while loop will break in only two cases
    # First if user used all the fund values. Second if user types "n" for no addition of unit.
    while playerTwoFunds >= 1:
        p=input("If u want to add unit hit y or n not to add =")
        if(p=="y"):
            option()
            r = input("Your Selection =")
            if r == "1":
                if (playerTwoFunds >= 2):
                    armyTwoList.append("Archer")
                    playerTwoFunds = playerTwoFunds - 2
                    print("Your remaining funds is = $" + str(playerTwoFunds))
                else:
                    print("You dont't have sufficient fund to buy this unit")
            elif r == "2":
                if (playerTwoFunds >= 1):
                    armyTwoList.append("Soldier")
                    playerTwoFunds = playerTwoFunds - 1
                    print("Your remaining funds is = $" + str(playerTwoFunds))
                else:
                    print("You dont't have sufficient fund to buy this unit")
            elif r == "3":
                if (playerTwoFunds >= 2):
                    armyTwoList.append("Knight")
                    playerTwoFunds = playerTwoFunds - 2
                    print("Your remaining funds is = $" + str(playerTwoFunds))
                else:
                    print("You dont't have sufficient fund to buy this unit")
            elif r=="4" :
                if(playerTwoFunds >= 2) :
                    armyTwoList.append("Siege Equipment")
                    playerTwoFunds = playerTwoFunds - 2
                    print("Your remaining funds is = $" + str(playerTwoFunds))
                else :
                    print("You dont't have sufficient fund to buy this unit")
            elif r=="5" :
                if (playerTwoFunds >= 3):
                    armyTwoList.append("Wizard")
                    playerTwoFunds = playerTwoFunds - 3
                    print("Your remaining funds is = $" + str(playerTwoFunds))
                else:
                    print("You dont't have sufficient fund to buy this unit")
            # If user input anything other than 1,2,3, you selected wrong input message will be rendered

            else :
                print("You selected wrong option")
        # If user hits "n", the loop will break and user will no longer be able to append unit
        elif p=="n" :
            break
        # Else if user types anything other than "y" or "n",Invalid selection message will be rendered.
        else :
            print("Invalid Selection")
    print("Player TWO your army units list is = " + str(armyTwoList))
    armyTwoRemainingFunds = playerTwoFunds
    print("Your remaining fund is = $" + str(armyTwoRemainingFunds))
    print("\n")
"""
Two lists are passed in combat function and the units in these two list battle with each other. After every outcome one 
unit is popped and the next unit from both lists get ready for the fight.
"""
def combat(armyOneList, armyTwoList):
    armyOneListIndex = 0
    armyTwoListIndex = 0
    storeArmyOnePoppedList = []
    storeArmyTwoPoppedList = []
    value = 1
    print("*-*-* Player One and Player Two Units Combat Outcome *-*-*")
    print("\n")
    """
    medics is used When a unit dies , it will be returned to the pool at the back of the army. Each time this happens, 
    supplies for the medics decreases. Once the medics have no supplies left, they will be unable to save any more units.  
    """
    def medics(a) :
        global armyOneRemainingFunds
        global armyTwoRemainingFunds
        if(a=="tie") :
            storeArmyOnePoppedList.append(armyOneList.pop(0))
            storeArmyTwoPoppedList.append(armyTwoList.pop(0))
            if (armyOneRemainingFunds >= 1):
                armyOneList.append(storeArmyOnePoppedList.pop(0))
                armyOneRemainingFunds = armyOneRemainingFunds - 1
            if (armyTwoRemainingFunds >= 1):
                armyTwoList.append(storeArmyTwoPoppedList.pop(0))
                armyTwoRemainingFunds = armyTwoRemainingFunds - 1
        elif a=="player one won" :
            storeArmyTwoPoppedList.append(armyTwoList.pop(0))
            if (armyTwoRemainingFunds >= 1):
                armyTwoList.append(storeArmyTwoPoppedList.pop(0))
                armyTwoRemainingFunds = armyTwoRemainingFunds - 1
        elif a=="player two won" :
            storeArmyOnePoppedList.append(armyOneList.pop(0))
            if (armyOneRemainingFunds >= 1):
                armyOneList.append(storeArmyOnePoppedList.pop(0))
                armyOneRemainingFunds = armyOneRemainingFunds - 1

    # While loop for players units fight, loop value is always true because "while loop variable" is not changing.
    # So, while loop will break iff any one player or both players army units list is empty.
    while (value <= 20):
        # In below three if and else conditions length of every army list is determined.
        # If even one of the list is empty final result of the combat will be declared.
        if (len(armyOneList) == 0 and len(armyTwoList) == 0):
            print("\n")
            print("No outcome. Match is a tie")
            break
        elif (len(armyTwoList) == 0):
            print("\n")
            print("All units of army two are dead so army one is the winner")
            break
        elif (len(armyOneList) == 0):
            print("\n")
            print("All units of army one are dead so army two is the winner")
            break
        # Real combat betwwen players units is starting from here
        # When result of combat is a tie both players one unit is popped for next unit to start the combat
        # When player one unit wins player two current unit is popped for next unit of player two to continue the battle.
        # When player two unit wins player one current unit is popped for next unit of player one to continue the battle.
        if armyOneList[armyOneListIndex] == "Archer" and armyTwoList[armyTwoListIndex] == "Archer":
            print("---Tie---")
            medics("tie")
        elif armyOneList[armyOneListIndex] == "Archer" and armyTwoList[armyTwoListIndex] == "Soldier":
            print("Archer from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Archer" and armyTwoList[armyTwoListIndex] == "Knight":
            print("Knight from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Archer" and armyTwoList[armyTwoListIndex] == "Siege Equipment":
            print("Siege Equipment from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Archer" and armyTwoList[armyTwoListIndex] == "Wizard":
            print("Archer from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Soldier" and armyTwoList[armyTwoListIndex] == "Archer":
            print("Archer from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Soldier" and armyTwoList[armyTwoListIndex] == "Soldier":
            print("Tie")
            medics("tie")
        elif armyOneList[armyOneListIndex] == "Soldier" and armyTwoList[armyTwoListIndex] == "Knight":
            print("Soldier from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Soldier" and armyTwoList[armyTwoListIndex] == "Siege Equipment":
            print("Siege Equipment from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Soldier" and armyTwoList[armyTwoListIndex] == "Wizard":
            print("Wizard from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Knight" and armyTwoList[armyTwoListIndex] == "Archer":
            print("Knight from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Knight" and armyTwoList[armyTwoListIndex] == "Soldier":
            print("Soldier from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Knight" and armyTwoList[armyTwoListIndex] == "Knight":
            print("Tie")
            medics("tie")
        elif armyOneList[armyOneListIndex] == "Knight" and armyTwoList[armyTwoListIndex] == "Siege Equipment":
            print("Knight from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Knight" and armyTwoList[armyTwoListIndex] == "Wizard":
            print("Wizard from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Siege Equipment" and armyTwoList[armyTwoListIndex] == "Archer":
            print("Seige Equipment from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Siege Equipment" and armyTwoList[armyTwoListIndex] == "Soldier":
            print("Seige Equipment from amry 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Siege Equipment" and armyTwoList[armyTwoListIndex] == "Knight":
            print("Knight From army 2 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Siege Equipment" and armyTwoList[armyTwoListIndex] == "Siege Equipment":
            print("Tie")
            medics("tie")
        elif armyOneList[armyOneListIndex] == "Siege Equipment" and armyTwoList[armyTwoListIndex] == "Wizard":
            print("Wizard from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Wizard" and armyTwoList[armyTwoListIndex] == "Archer":
            print("Archer from army 2 won")
            medics("player two won")
        elif armyOneList[armyOneListIndex] == "Wizard" and armyTwoList[armyTwoListIndex] == "Soldier":
            print("Wizard from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Wizard" and armyTwoList[armyTwoListIndex] == "Knight":
            print("Wizard from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Wizard" and armyTwoList[armyTwoListIndex] == "Siege Equipment":
            print("Wizard from army 1 won")
            medics("player one won")
        elif armyOneList[armyOneListIndex] == "Wizard" and armyTwoList[armyTwoListIndex] == "Wizard":
            print("Tie")
            medics("tie")
print("Player one you have $10 make your army selection ")
appendUnitsToArmyOne()
print("Player two you have $10 make your army selection ")
appendUnitsToArmyTwo()
combat(armyOneList,armyTwoList)