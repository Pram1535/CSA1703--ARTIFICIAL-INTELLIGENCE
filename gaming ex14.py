def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, "O"):
        return -1
    if check_win(board, "X"):
        return 1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_eval = -float("inf")
    best_move = None
    alpha = -float("inf")
    beta = float("inf")

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
                alpha = max(alpha, eval)

    return best_move

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Let's play Tic-Tac-Toe!")

    while True:
        print_board(board)
        row, col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())

        if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = "O"

            if check_win(board, "O"):
                print_board(board)
                print("You win!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = "X"

            if check_win(board, "X"):
                print_board(board)
                print("AI wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_tic_tac_toe()
