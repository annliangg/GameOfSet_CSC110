
# Annie Liang
# CSC 110 - Fall 2022
# Programming Project - Set
# Due Date: Dec 13

import random

# Create list with all 81 possible cards
def createDeck():
    # Necessary variables
    deckList = []
    card = ""

    # Possible features (excluding the numbers)
    color = ['R','G','P']
    shade = ['S', 'O', 'P']
    shape = ['O', 'S', 'D']

    # Loop through 81 times (3*3*3*3)
    for i in range(1, 4):
      for j in range(3):
        for k in range(3):
          for l in range(3):
            # Cycle through each feature in the lists and add to list
            card = str(i)+color[j]+shade[k]+shape[l]
            deckList.append(card)
     
    return deckList

# Check for duplicates in a list
def checkDup(card, list1):
    if card in list1:
        # Duplicate card
        return True
    else:
        # No duplicates
        return False

# Randomly generate 12 cards into a play deck list
def generatePlayCards(deckList):
    # Initialize card list
    cardList = []

    # Randomly pick and put 12 cards into list (Without replacement)
    done = False
    
    # Add first random card from deckList
    card = deckList[random.randint(0,80)]
    cardList.append(card)
    
    while done == False:
        # Draw new card
        card = deckList[random.randint(0,80)]
        
        # Check for duplicates
        valid = False
        while valid == False:
            # If duplicate found, redraw card
            if checkDup(card, cardList):
                card = deckList[random.randint(0, 80)]
            else:
                valid = True

        # Add card to list after checking for duplicates
        cardList.append(card)
                
        # End Loop (12 Cards Picked)
        if len(cardList) == 12:
            done = True

    return cardList

# Display the 12 play cards
def displayPlayCards(cardList):
    # Print 4 cards per row, 3 rows
    row = ""
    index = 0
    # 3 Rows
    for i in range(1, 4):
        # 4 cards per row
        for j in range(4):
            row += cardList[index] + " "
            index += 1

        # Print row and clear string for next iteration
        print(row)
        row = ""

# Take user input to create set
def createSet(cardList):
    # Initialize list
    setList = []

    # User input for 3 cards from play list
    for i in range(1, 4):
        
        # Check conditions
        valid = False
        while valid == False:
            card = input(str(i)+": ")
            
            # Check if card is in play list
            if checkDup(card, cardList):
                
                # Check if card was previously inputted
                if (not checkDup(card, setList)):
                    valid = True
                else:
                    print("You have already chosen that card, please try again")
            else:
                print("Not a valid choice, please choose again")
                    
        # Add card to list after checking conditions
        setList.append(card)
        
    # Extra blank line
    print("")
    return setList

# Check if features are the same
def same(testList, pos):
    # Start as true
    isSame = True
    
    # Start from index 1 (second item in the list)
    for i in range(1, len(testList)):

        # Compares the character of the current card with the previous card index
        if not (testList[i-1][pos] == testList[i][pos]):
            # Feature is not the same in each card
            isSame = False

    return isSame

# Check if features are different
def diff(testList, pos):
    # Start as true
    isDiff = True
    
    # Loop through the amount of cards
    for i in range(len(testList)):
        
        # Compare between characters in each card
        for j in range(i + 1, len(testList)):
            
            # If a character is the same
            if (testList[i][pos] == testList[j][pos]):
                # The feature is not different in each card
                isDiff = False

    return isDiff

# Compare function (Reduce redundancy)
def compare(testList, pos):
    return (same(testList,pos) or diff(testList, pos))

# Check if the user inputted set is actually a set
def isSET(testList):
    # Start as true 
    isSet = True
    
    # Loop through the length of the card (each feature)
    for i in range(4):
        # Compares all cards at the same index (if not all the same or different)
        if (compare(testList, i) == False):
            # Cards are not a set
            isSet = False
    
    return isSet

# Ask user for next move 
def nextMove():
    # Prints messages
    print("What would you like to do next?")
    print("F - Find another SET\nD - Deal another set of cards\nQ - Quit")

    # User input
    choice = input("==>")

    # Test for valid user input
    valid = False
    while valid == False:
        if (choice == "F" or choice == "D" or choice == "Q"):
            valid = True
            return choice
        else:
            choice = input("Bad input, try again ==>")

# Play the game 
def playGame(cardList):
    # Print message
    print("Choose three cards that make a SET\n")

    # User inputs set
    testSet = createSet(cardList)

    # Test if user input is actually a set
    validSet = isSET(testSet)
    if validSet == True:
        print("YES that is a SET\n")
    else:
        print("Sorry, that is not a SET\n")

    # Ask user for next move
    return nextMove()
        
# Main function
def main(seedIn):
    random.seed(seedIn)
    # Print game instructions
    print("Choose a SET from the following cards.\nA SET consists of three cards where each feature is EITHER the same\non each card, or different on each card.\n")

    # Intial choice is D to start game
    choice = "D"

    # Keep playing game until user inputs Q
    done = False
    while done == False:
        # Choice is Deal another set of cards
        if choice == "D":
            # Play game with new deck
            cardList = generatePlayCards(createDeck())

            # Display the 12 cards in playing deck
            displayPlayCards(cardList)
            
            choice = playGame(cardList)
        # Choice is Find another SET
        elif choice == "F":
            choice = playGame(cardList)
            
        # Choice is Quit
        else:
            print("\nGame Over - Thanks for Playing...")
            # End loop
            done = True
        
