def print_board(board):
    print("---------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(" " + cell + " ", end="|")
        print("\n---------")


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def play_game():
    board = [[" ", " ", " "] for _ in range(3)]
    current_player = "X"
    winner = None
    num_moves = 0

    while winner is None and num_moves < 9:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                break
            else:
                print("Invalid move. Try again.")

        board[row][col] = current_player
        num_moves += 1
        winner = check_winner(board)
        current_player = "O" if current_player == "X" else "X"

    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

play_game()
