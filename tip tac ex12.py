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
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Let's play Tic-Tac-Toe!")
    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (e.g., 1 2): ").split())
        if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
if __name__ == "__main__":
    play_tic_tac_toe()
