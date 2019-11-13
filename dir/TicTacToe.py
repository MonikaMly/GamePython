X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def intructions():
    """Display Instructions."""
    print(
        """
        Enter number from range 0 - 8.
        It is associated with the numbr from the following board:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

        """
    )

def askYesNo(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def askQuestion(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
        return response

def pieces():
    goFirst = askYesNo("Do you want to start the game? (y/n): ")
    if goFirst == "y":
        print("You start X")
        gamer = X
        computer = O
    else:
        print("Computer has the first move")
        computer = X
        gamer = O
    return computer, gamer

def newBoard():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def displayBoard(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legalMoves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return  moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def gamerMove(board, gamer):
    legal = legalMoves(board)
    move = None
    while move not in legal:
        move = askQuestion("What is your move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThis move is illegal, choose different one\n")
    print("Znakomicie...")
    return move


def computer_move(board, computer, gamer):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I choose", end=" ")

    for move in legalMoves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legalMoves(board):
        board[move] = gamer
        if winner(board) == gamer:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legalMoves(board):
            print(move)
            return move

def nextTurn(turn):
    if turn == X:
        return O
    else:
        return X

def congratWinner(theWinner, computer, gamer):

    if theWinner != TIE:
        print(theWinner, "is the winner!\n")
    else:
        print("Tie!\n")

    if theWinner == computer:
        print("Computer won")

    elif theWinner == gamer:
        print("Gamer won")

    elif theWinner == TIE:
        print("It is a tie")

def main():
    intructions()
    computer, gamer = pieces()
    turn = X
    board = newBoard()
    displayBoard(board)

    while not winner(board):
        if turn == gamer:
            move = gamerMove(board, gamer)
            board[move] = gamer
        else:
            move = computer_move(board, computer, gamer)
            board[move] = computer
        displayBoard(board)
        turn = nextTurn(turn)

    the_winner = winner(board)
    congratWinner(the_winner, computer, gamer)

main()
