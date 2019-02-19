
def covering_board(row_p, col_p, board, white_space):
    global block_j, block_i
    global count

    if white_space == 0:
        count += 1
    elif row_p >= len(board):
        return
    elif col_p >= len(board[row_p]):
        return covering_board(row_p+1, 0, board, white_space)
    elif board[row_p][col_p] == 1:
        covering_board(row_p, col_p+1, board, white_space)
    else:
        for i in range(0, len(block_i)):
            if set(board, row_p, col_p, 0, 1, block_i[i], block_j[i]):
                covering_board(row_p, col_p+1, board, white_space - 3)
            set(board, row_p, col_p, 0, -1, block_i[i], block_j[i])

def set(board, y, x, _type, delta, block_i, block_j):
    ok = True
    for i in range (0,3):
        ny = y + block_i[i]
        nx = x + block_j[i]
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        else:
            board[ny][nx] += delta
            if(board[ny][nx] > 1):
                ok = False
    return ok


if __name__ == "__main__":
    global block_j, block_i
    global count
    block_i = [[0, 1, 1], [0, 1, 1], [0, 0, 1], [0, 0, 1]]
    block_j = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, 1, 1]]

    test_case = int(input())

    while test_case > 0:
        count = 0
        initial_board = []
        row, col = map(int, input().split(' '))
        white_space = 0
        for i in range(row):
            column = []
            for cell in input():
                if cell == '.':
                    column.append(0)
                    white_space += 1
                elif cell == '#':
                    column.append(1)
            initial_board.append(column)
        if white_space % 3 != 0:
            print(0)
        else:
            covering_board(0, 0, initial_board, white_space)
            print(count)

        test_case -= 1
