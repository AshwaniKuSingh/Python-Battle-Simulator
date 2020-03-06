""""                  *-*-*Overview*-*-*
This program consist of two function
1. appendUnitsToArmy() function for appending units to the army.
2. combat(armyOneList,armyTwoList) function to begin the fight between player one and player two units.
"""
armyOneList = list()
armyTwoList = list()
"""
appendUnitsToArmy() function to append the units to army to list that is passed as parameters and this function 
returns the remaining fund available to players and player list is established. 
"""
def appendUnitsToArmy(appendUnits):
    playerFunds=10
    # The while loop will break in only two cases
    # First if user used all the fund values. Second if user types "n" for no addition of unit.
    while playerFunds >= 1:
        p=input("If u want to add unit hit y or n not to add =")
        if(p=="y"):
            print("1.Archer")
            print("2.Soldier")
            print("3.Knight")
            r = input("Your Selection =")
            if r == "1":
                appendUnits.append("Archer")
                playerFunds = playerFunds - 1
                print("Your remaining funds is = $" + str(playerFunds))
            elif r == "2":
                appendUnits.append("Soldier")
                playerFunds = playerFunds - 1
                print("Your remaining funds is = $" + str(playerFunds))
            elif r == "3":
                appendUnits.append("Knight")
                playerFunds = playerFunds - 1
                print("Your remaining funds is = $" + str(playerFunds))
            # If user input anything other than 1,2,3, you selected wrong input message will be rendered
            else :
                print("You selected wrong option")
        # If user hits "n", the loop will break and user will no longer be able to append unit
        elif p=="n" :
            break
        # Else if user types anything other than "y" or "n",Invalid selection message will be rendered.
        else :
            print("Invalid Selection")
    return playerFunds
"""
Two lists are passed in combat function and the units in these two list battle with each other. After every outcome one 
unit is popped and the next unit from both lists get ready for the fight.
"""
def combat(armyOneList,armyTwoList) :
    armyOneListIndex=0
    armyTwoListIndex=0
    whileLoopValue=1
    print("*-*-* Player One and Player Two Units Combat Outcome *-*-*")
    print("\n")
    # While loop for players units fight, loop value is always true because "while loop variable" is not changing.
    # So, while loop will break iff any one player or both players army units list is empty.
    while(whileLoopValue<=2) :
        # In below three if and else conditions length of every army list is determined.
        # If even one of the list is empty final result of the combat will be declared.
        if(len(armyOneList)==0 and len(armyTwoList)==0):
            print("\n")
            print("No outcome. Match is a tie.")
            break
        elif(len(armyTwoList)==0) :
            print("\n")
            print("Player two has no unit so player one is the winner.")
            break
        elif(len(armyOneList)==0):
            print("\n")
            print("Player one has no unit so player two is the winner.")
            break
        # Real combat betwwen players units is starting from here
        # When result of combat is a tie both players one unit is popped for next unit to start the combat
        # When player one unit wins player two current unit is popped for next unit of player two to continue the battle.
        # When player two unit wins player one current unit is popped for next unit of player one to continue the battle.
        if armyOneList[armyOneListIndex]=="Archer" and armyTwoList[armyTwoListIndex]=="Archer" :
            print("---Tie---")
            armyOneList.pop(0)
            armyTwoList.pop(0)
        elif armyOneList[armyOneListIndex]=="Archer" and armyTwoList[armyTwoListIndex]=="Soldier" :
            print("Archer from army 1 won")
            armyTwoList.pop(0)
        elif armyOneList[armyOneListIndex]=="Archer" and armyTwoList[armyTwoListIndex]=="Knight" :
            print("Knight from army 2 won")
            armyOneList.pop(0)
        elif armyOneList[armyOneListIndex]=="Soldier" and armyTwoList[armyTwoListIndex]=="Archer" :
            print("Archer from army 2 won")
            armyOneList.pop(0)
        elif armyOneList[armyOneListIndex]=="Soldier" and armyTwoList[armyTwoListIndex]=="Soldier" :
            print("---Tie---")
            armyOneList.pop(0)
            armyTwoList.pop(0)
        elif armyOneList[armyOneListIndex]=="Soldier" and armyTwoList[armyTwoListIndex]=="Knight" :
            print("Soldier from army 1 won")
            armyTwoList.pop(0)
        elif armyOneList[armyOneListIndex]=="Knight" and armyTwoList[armyTwoListIndex]=="Archer" :
            print("Knight from army 1 won")
            armyTwoList.pop(0)
        elif armyOneList[armyOneListIndex]=="Knight" and armyTwoList[armyTwoListIndex]=="Soldier" :
            print("Soldier from army 2 won")
            armyOneList.pop(0)
        elif armyOneList[armyOneListIndex]=="Knight" and armyTwoList[armyTwoListIndex]=="Knight" :
            print("---Tie---")
            armyOneList.pop(0)
            armyTwoList.pop(0)
print("Player one you have $10 make your army selection ")
armyOneRemainingFund=appendUnitsToArmy(armyOneList)
print("Player one your army units list is = " + str(armyOneList))
print("Your remaining fund is = $" + str(armyOneRemainingFund))
print("\n")
print("Player two you have $10 make your army selection ")
armyTwoRemainingFund=appendUnitsToArmy(armyTwoList)
print("Player Two your army units list is = " + str(armyTwoList))
print("Your remaining fund is = $" + str(armyTwoRemainingFund))
print("\n")
combat(armyOneList,armyTwoList)
