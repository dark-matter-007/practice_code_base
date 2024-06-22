import random

from art import *

tprint("Tic Tac Toe")
print("::: THIS PROGRAM IS AN EXPERIMENT FOR DESIGNING AI TO COMPETE AGAINST HUMAN :::\n")
class GameState:
    # Here player turn 0 means human, and eval 1 means preferable
    playerLocations, playerTurn, evaluation = [], bool(0), bool(1)

    def init_game_state():
        # here 0 for human and 1 for bot
        GameState.playerLocations = [2,2,2,
                                     2,2,2,
                                     2,2,2]

        GameState.playerTurn = True

    def get_state():
        return GameState.playerLocations

    def set_state(index_to_set):
        GameState.playerLocations[index_to_set] = int(0)

    def setCurrentStackAs(stack):
        GameState.playerLocations = stack


GameState.init_game_state()

def move_of_ai(game_state_list):
    stateStack = game_state_list
    moveableStack = []
    possibleStacksAfterMove = []

    # Check for all the possibilities where the AI can move
    for position in stateStack:
        if position != 0 and position != 2:
            moveableStack.append(True)
        else:
            moveableStack.append(False)

    # decide among them, which one will be the best... for this predict human's next turn
    counter = 0
    for i in moveableStack:
        if i == True:
            stateStack[counter] = 1
            possibleStacksAfterMove.append(stateStack)

def run_game_check_algorithm(gameState):
    print("checking algorithm is running on this stack : ", gameState)
    buffer = []
    initialState = list(gameState)
    for element in initialState:
        buffer.append(element)
    print("initially buffer is ", buffer)

    blockTheseStates =   [[1,2], [1,3], [2,3],
                          [4,6], [4,5], [5,6],
                          [7,8], [8,9], [7,9],
                          [1,7], [1,4], [4,7],
                          [2,8], [2,5], [5,8],
                          [3,6], [3,9], [6,9],
                          [1,9], [1,5], [5,9],
                          [7,5], [3,5], [7,3]]
    blockTechniques = [3,2,1,
                       5,6,4,
                       9,7,8,
                       4,7,1,
                       5,8,2,
                       9,6,3,
                       5,9,1,
                       3,7,5]
    for indexPair in blockTheseStates:
        print("Checking index pair ", indexPair)
        if (initialState[indexPair[0]-1] == 0) and (initialState[indexPair[1]-1] == 0) and (initialState[blockTechniques[blockTheseStates.index(indexPair)]-1] != 1):
            blockTheseStatesIndex = blockTheseStates.index(indexPair)
            targetIndex = blockTechniques[blockTheseStatesIndex]-1
            initialState[targetIndex] = 1 # bot's turn
            break

    if buffer == initialState: # means the AI bot did not find any place to block user's turn
        possibleMoves = []
        for index in range(len(initialState)):
            if initialState[index] == 2:
                possibleMoves.append(index)

        moveBuffer = []
        for move in possibleMoves:
            newState = initialState
            newState[move] = 1
            moveBuffer.append(newState)

        for humantTurnMove in moveBuffer:
            possibleMoves = []
            for index in range(len(humantTurnMove)):
                if initialState[index] == 2:
                    possibleMoves.append(index)

            newHumanMoveBuffer = []
            ind, dueToIndex = 0, 0
            for move in possibleMoves:
                newState = moveBuffer[ind]
                newState[move] = 0
                dueToIndex = ind
                ind += 1
                newHumanMoveBuffer.append([newState, dueToIndex])

        for futureGameStateList in newHumanMoveBuffer:
            # check if human will win in next move, and then block him
            futureGameState = futureGameStateList[0]
            for indexPair in blockTheseStates:
                if (futureGameState[indexPair[0] - 1] == 0) and (futureGameState[indexPair[1] - 1] == 0) and (
                        futureGameState[blockTechniques[blockTheseStates.index(indexPair)] - 1] != 1):
                    newHumanMoveBuffer.remove(futureGameStateList)
                    break

        ChosenMove = 0
        if len(newHumanMoveBuffer) == 0:
            possibleMoves = []
            print ("length of the buffer is : ", len(buffer))
            for index in range(len(buffer)):
                print("took index = ", index)
                print (buffer)
                if buffer[index] == 2:
                    print("appended ", index, "to possibleMoves")
                    possibleMoves.append(index)
            ChosenMove = random.choice(possibleMoves)
            newState = initialState
            newState[ChosenMove] = 1
            moveBuffer.clear()
            moveBuffer.append(newState)
        else:
            goodMoves, moveBuffer = [], []
            for goodMove in newHumanMoveBuffer:
                goodMoves.append(goodMove[2])
            for goodMove in goodMoves:
                newState = buffer
                newState[goodMove] = 1
                moveBuffer.append(newState)

        if len(moveBuffer) > 1:
            initialState = moveBuffer[random.randint(0, len(moveBuffer))]
        else:
            initialState = moveBuffer[0]

    returnStack = initialState
    return returnStack


while True:
    printableState = GameState.get_state()
    if not (2 in printableState):
        break
    counter = 0
    for element in printableState:
        if element == 0:
            element = "o"
        elif element == 1:
            element = "x"
        else :
            element = "."

        if counter == 3:
            print("")
            counter = 0
        print(element, end="\t")
        counter += 1
    print("")

    playerInput = input("Enter 1 to 9 for putting 'o' as your turn : ")

    if playerInput.isnumeric():
        GameState.set_state(int(playerInput)-1)

    GameState.setCurrentStackAs(run_game_check_algorithm(GameState.get_state()))