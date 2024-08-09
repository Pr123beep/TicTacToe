def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(board[i] == mark for i in condition) for condition in win_conditions)


def check_draw(board):
    return all(cell != ' ' for cell in board)


def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                return move
            else:
                print("Move must be between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        move = get_move()
        if board[move] == ' ':
            board[move] = current_player
        else:
            print("That cell is already taken. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
