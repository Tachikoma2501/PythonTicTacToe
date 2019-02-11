
# Install the PILLOW package so images can be used
from PIL import Image, ImageDraw

#HAL9000 = Image.open('Hal9000.jpg')
#HAL9000.show()

# This creates the Tic Tac Toe game board
gameBoard = [' ' for x in range(10)]

# This defines the letterInput and allows a given letter to be inserted into a selected position
def letterInput(letter, position):
    gameBoard[position] = letter

# This will check the selected space and return tree or not if that space is free/empty or not
def freeSpace(position):
    return gameBoard[position] == ' '

#This will not only display a visual game board for the user to see to play tic tac toe
#But this also defines the spaces/positions (1-9) within each square for the letter to
#be inserted into
def createGameBoard(gameBoard):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('    |    |')
    print(' ' + gameBoard[1] + '  | ' + gameBoard[2] + '  | ' + gameBoard[3])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + gameBoard[4] + '  | ' + gameBoard[5] + '  | ' + gameBoard[6])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + gameBoard[7] + '  | ' + gameBoard[8] + '  | ' + gameBoard[9])
    print('    |    |')

# This gives the perameters for what determines a victory
def determineWinner(board, playerLetter):
    return((board[7] == playerLetter and board[8] == playerLetter and board[9] == playerLetter) or # If across bottom row
           (board[4] == playerLetter and board[5] == playerLetter and board[6] == playerLetter) or # If across middle row
           (board[1] == playerLetter and board[2] == playerLetter and board[3] == playerLetter) or # If across top row
           (board[7] == playerLetter and board[4] == playerLetter and board[1] == playerLetter) or # If from bottom left to top left
           (board[8] == playerLetter and board[5] == playerLetter and board[2] == playerLetter) or # If from bottom middle to top middle
           (board[9] == playerLetter and board[6] == playerLetter and board[3] == playerLetter) or # If from bottom right to top right
           (board[7] == playerLetter and board[5] == playerLetter and board[3] == playerLetter) or # If diagonally from bottom left to top right
           (board[9] == playerLetter and board[5] == playerLetter and board[1] == playerLetter))   # If diagonally from top left to bottom right

#This defines the function for the players turn actions
def playerTurn():
    #runs while True
    run = True
    #while loop
    while run:
        #prompts the user to choose a space to place their marker in
        turn = input('Choose your space: ')
        try: # Try statement
            turn = int(turn) #if statement for when the turn is greater than 0 but less than 10
            if turn > 0 and turn < 10:
                if freeSpace(turn): # if a space is free
                    run = False
                    letterInput('X', turn)
                else: # else statements which also print messages
                    print('Hal9000: Error, that location has already been taken.')
            else:
                print('Hal9000: Please enter a number within the given range.')
        except: # Except statement
            print('Hal9000: Please enter a number within the given range.')

# This defines the function for the computer's turn
def hal9000Turn():
    # Views the current available moves possible and determines where to place the marker
    # depending on several variables such as players marker placement and possible other factors for x
    availableMoves = [x for x, letter in enumerate(gameBoard) if letter == ' ' and x != 0]
    turn = 0
    # for loop for the available moves for i with the X & O in conjunction with
    # The gameboard to determine next move
    for let in ['O', 'X']:
        for i in availableMoves:
            gameBoardCopy = gameBoard[:]
            gameBoardCopy[i] = let
            if determineWinner(gameBoardCopy, let):
                turn = i
                return turn

    # This determines if the corners on the game board are open or filled
    ifCornersOpen = [] #defines the ifCornersOpen as empty
    #for loop for i defining the corners as the array of numerical positions
    for i in availableMoves:
        if i in [1, 3, 7, 9]:
            ifCornersOpen.append(i)
    # if statement for is the "ifCornerOpen" is greater than 0
    # The computer will then choose a random corner to place their marker in
    if len(ifCornersOpen) > 0:
        turn = randomizer(ifCornersOpen)
        return turn
    # if statement for when the middle space is available
    if 5 in availableMoves:
        turn = 5
        return turn
    # defines the function for when the edge spaces are available
    # these spaces are defined as the numerical array presented in the for loop with i
    ifEdgesOpen = []
    for i in availableMoves:
        if i in [2, 4, 6, 8]:
            ifEdgesOpen.append(i)
    # an if statement for when the ifEdgesOpen is greater than 0
    # then the computer will choose a random edge space
    if len(ifEdgesOpen) > 0:
        turn = randomizer(ifEdgesOpen)

    return turn
# This defines the randomizer, importing the random feature in python
# and gives the rang for it
def randomizer(ri):
    import random
    ln = len(ri)
    rn = random.randrange(0, ln)
    return ri[rn]
# defines the function for is the game board was filled and no more
# spaces were available
def ifGameBoardFull(gameBoard):
    #if statement for if the spaces within the gameBoard were greater than 1, return False
    if gameBoard.count(' ') > 1:
        return False
    else:# else statement would return True
        return True
# The main function which will print the messages and runs the functions to run the tic-tac-toe game
def main():
    print('Hal9000: Welcome')
    print('Hal9000: This is a low difficulty cognitive test using the simple game "Tic-Tac-Toe" ')
    print('Hal9000: I am a simple A.I. that will serve as your opponent, I was given the name "Hal9000". ')
    print('Hal9000: Use the keyboard to choose which space to place your mark "X" in using number 1-9')
    print('Hal9000: 1-9 corresponds with the spaces starting from the top left space and going right')
    print('Hal9000: The first one to have a full row of their given letter is the winner')
    print('Hal9000: Otherwise, the game will result in a tie')
    print('Hal9000: While passing this test may seem difficult, winning is possible with the correct moves')
    print('Hal9000: Explanation concluded')
    print('Hal9000: Starting game')
    # This prints out the games board to the user in the terminal window
    createGameBoard(gameBoard)
    # while not loop to check if the gameboard is full
    while not(ifGameBoardFull(gameBoard)):
        # if not statement for if the computer has not won, then run playerTurn
        if not(determineWinner(gameBoard, 'O')):
            playerTurn()
            #shows the current gameBoard with current markers
            createGameBoard(gameBoard)
        else: #else statement, print message
            print('Hal9000: Test Failure, please try again')
            break
        # if not statement for if the player has not won, then run hal9000Turn
        if not(determineWinner(gameBoard, 'X')):
            turn = hal9000Turn()
            # if statement for if no further moves can be made an no winner is determined
            if turn == 0:
                print('Hal9000: How unfortunate, it seems to be a tie')
            else: # else statement which has the computer places their marker
                letterInput('O', turn)
                print('Hal9000 has placed a "O" in the position ', turn, ':')
                createGameBoard(gameBoard)
        else: # else statement for if the player wins
            print('Hal9000: Congratulation, You have passed and won this game')
            break
    # if statement for if the gameBoard is full and no further moves can be made
    if ifGameBoardFull(gameBoard):
        print('Hal9000: How unfortunate, it seems to be a tie.')
        print('Hal9000: No further moves can be made')
# A while true loop to ask the user if they wish to run the program
while True:
    print('Start program?')
    print('Y (for yes) or N (for no)')
    # prompts the user to input their answer
    answer = input('Enter: ')
    # if statement to take the user input and making it lower case for either y or yes
    # and if yes, then running the gameBoard and main functions
    if answer.lower() == 'y' or answer.lower == 'yes':
        gameBoard = [' ' for x in range(10)]
        main()
    else:
        # else statement, ending the [program
        break