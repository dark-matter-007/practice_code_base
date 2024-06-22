import java.util.Random;
import java.util.Scanner;


class NGame {
    //  Variables
    public int[] gameState = new int[9]; // each element for each square || 2 for empty | 1 for computer | 0 for human
    int[] defaultState;
    int[][] blockTheseStates =   {{1, 2}, {1, 3}, {2, 3},
            {4, 6}, {4, 5}, {5, 6},
            {7, 8}, {8, 9}, {7, 9},
            {1, 7}, {1, 4}, {4, 7},
            {2, 8}, {2, 5}, {5, 8},
            {3, 6}, {3, 9}, {6, 9},
            {1, 9}, {1, 5}, {5, 9},
            {7, 5}, {3, 5}, {7, 3}};
    int[] blockTechniques =   {3, 2, 1,
            5, 6, 4,
            9, 7, 8,
            4, 7, 1,
            5, 8, 2,
            9, 6, 3,
            5, 9, 1,
            3, 7, 5};

    public NGame() {
        System.out.println("New Game Started!");
        // set all the squares on the board as empty
        for (int index = 0; index <= 8; ++index){
            gameState[index] = 2;
        }

        defaultState = gameState.clone();
    }
    public void printState() {
        int counter = 0;
        for(int element : gameState){
            if (counter == 3) {
                System.out.println();
                counter = 0;
            }

            if (element == 2) {
                System.out.print(".\t");
            } else if (element == 1) {
                System.out.print("x\t");
            } else {
                System.out.print("0\t");
            }
            ++counter;
        }
        System.out.println();
    }
    public void putPlayerCharAt(int playerChoice) {
        gameState[playerChoice-1] = 0;
    }
    private void aiMoveRandomly(){
        Random random = new Random();
        int aiChoice = random.nextInt(9);

        int[] possibleMoves = new int[9];
        int indexCounter = 0;
        int gameIndexCounter = 0; // here gameIndexCounter is referring to the blocks of tic tac toe game grid
        for ( int position : gameState ) {
            if (position == 2) {
                possibleMoves[indexCounter] = gameIndexCounter;
                ++indexCounter;
                ++gameIndexCounter;
            }
            else {
                ++gameIndexCounter;
            }
        }
        boolean isChoiceValid = false;
        while (!isChoiceValid) {
            for (int i = 0; i < indexCounter; i++) {
                if (possibleMoves[i] == aiChoice) {
                    isChoiceValid = true;
                    break;
                }
                else {
                    aiChoice = random.nextInt(9);
                }
            }
        }
        gameState[aiChoice] = 1;
    }
    private boolean checkIfComputerCanWin() {
        int freeSpaceCounter = 0;
        for (int pos : gameState){
            if (pos == 2) {
                ++freeSpaceCounter;
            }
        }
        int[] possibleMoves = new int[freeSpaceCounter];
        int indexCounter = 0;
        int gameIndexCounter = 0; // here gameIndexCounter is referring to the blocks of tic tac toe game grid
        for ( int position : gameState ) {
            if (position == 2) {
                possibleMoves[indexCounter] = gameIndexCounter;
                ++indexCounter;
            }
            ++gameIndexCounter;
        }

        int[][] futureDump = new int[possibleMoves.length][9];
        int [] stackDump = new int[9];
        indexCounter = 0;
        for (int move : possibleMoves) {
            stackDump = gameState.clone();
            stackDump[move] = 1;
            futureDump[indexCounter] = stackDump;
            ++indexCounter;
        }

        boolean foundWinningStack = false;
        int[] winningStack = new int[9];
        for (int[] stack : futureDump) {
            indexCounter = 0;
            for (int[] state : blockTheseStates) {
                if ((stack[state[0] - 1] == 1) && (stack[state[1] - 1] == 1) && (stack[blockTechniques[indexCounter]-1] == 1)) {
                    foundWinningStack = true;
                    break;
                }
                ++indexCounter;
                if (foundWinningStack){
                    winningStack = stack.clone();
                    break;
                }
            }
        }
        if (foundWinningStack) {
            gameState = winningStack.clone();
        }
        return foundWinningStack;
    }

    public void aiMove(){
        int[] initialState = gameState.clone();
        int[] resultState = initialState.clone();

        int indexCounter = 0;
        for (int[] blockStatePair : blockTheseStates) {
            if ((initialState[blockStatePair[0] - 1] == 0) && (initialState[blockStatePair[1] - 1] == 0) && (initialState[blockTechniques[indexCounter] - 1] == 2)) {
                resultState[blockTechniques[indexCounter] - 1] = 1;
                break;
            } else {
                ++indexCounter;
            }
        }

        boolean noChangeInResultState = true;
        indexCounter = 0;
        for (int element : resultState) {
            if (element != initialState[indexCounter]) {
                System.out.println("I blocked yours xD");
                noChangeInResultState = false;
                break;
            }
            indexCounter++;
        }

        if (noChangeInResultState) {
            boolean winningStackWasFound = checkIfComputerCanWin();
            if (!winningStackWasFound) {
                System.out.println("Doing random move :|");
                aiMoveRandomly(); // means move randomly
            }
        } else {
            gameState = resultState.clone();
        }


    }
    public boolean boardIsFull() {
        boolean isBoardFull = true;
        for (int index = 0; index < gameState.length; index++) {
            if (gameState[index] == 2){
                isBoardFull = false;
            }
        }
        return isBoardFull;
    }
    public boolean checkWinner() {
        int indexCounter = 0;
        for (int[] state : blockTheseStates) {
            if ((gameState[state[0]-1] == 0) && (gameState[state[1]-1] ==0) && (gameState[blockTechniques[indexCounter]-1] == 0) ){
                printState();
                System.out.println("Congratulations! You won!");
                return true;
            } else if ((gameState[state[0]-1] == 1) && (gameState[state[1]-1] ==1) && (gameState[blockTechniques[indexCounter]-1] == 1)) {
                printState();
                System.out.println("Oops! Computer Wins!");
                return true;
            } else {
                ++indexCounter;
            }
        }
        return false;
    }

    public void clearScreen(){
        System.out.println("\n".repeat(100));
    }

    public void think() throws InterruptedException {
        printState();
        System.out.println("Computer is thinking...");
        Thread.sleep(1000);
    }
}

class TicTacToeAIThatPrefersCutting {
    public static void main(String[] args) throws InterruptedException {

        // Taking user input for the first time
        Scanner scanner = new Scanner(System.in);
        System.out.println("This program is an Experimental AI language model that plays TicTacToe to compete against human");
        NGame game = new NGame();

        game.clearScreen();

        while (true) {

            game.printState();
            System.out.print("Enter your choice [1 to 9] : ");
            int playerChoice = scanner.nextInt();
            
            game.putPlayerCharAt(playerChoice);
            
            if (game.checkWinner()) {
                System.out.println( " [ winner instance detected ] " );
                break;
            }
            if (game.boardIsFull()) {
                game.printState();
                System.out.println(" [ draw instance detected ] ");
                System.out.println("\nIt's a tie! No One wins");
                break;
            }
            
            game.clearScreen();
            game.think();
            game.clearScreen();
            game.aiMove();
            
            if (game.checkWinner()) {
                break;
            }
        }
        
        scanner.close(); // finally close the scanner, when the user has input everything needed.
    }
}
