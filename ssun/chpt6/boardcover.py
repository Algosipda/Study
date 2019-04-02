def cover_board(i, j, board):
	global blocks

	if i == len(board):
			return 1

	elif j == len(board[i]):
		return cover_board(i+1, 0, board)

	elif board[i][j] == '#':
		return cover_board(i, j+1, board)

	else:
		res = 0
		for block in blocks:
			if is_usable_block(block, i, j, board):
				board = cover(block, i, j, board)
				res += cover_board(i, j+1, board)
				board = uncover(block, i, j, board)

		return res

def is_usable_block(block, i, j, board):
	for cell in block:
		row = i + cell[0]
		col = j + cell[1]
		if col < 0:
			return False
		elif row >= len(board) or col >= len(board[i]):
			return False
		elif board[row][col] == '#':
			return False
	return True

def cover(block, i, j, board):
	for cell in block:
		board[i+cell[0]][j+cell[1]] = "#"
	return board

def uncover(block, i, j, board):
	for cell in block:
		board[i+cell[0]][j+cell[1]] = '.'
	return board

def main():
	global blocks

	blocks = [
	[[0,0], [1,0], [1,1]],
	[[0,0], [0,1], [1,1]],
	[[0,0], [0,1], [1,0]],
	[[0,0], [1,0], [1,-1]]]

	test_case = int(input())

	while test_case > 0:
		row_size, col_size = map(int, input().split())
		white_space = 0
		board = []
		for i in range(0, row_size):
			col = []
			for cell in input():
				if cell == '.':
					white_space += 1
				col.append(cell)
			board.append(col)
		if not (white_space % 3 == 0):
			print(0)
		else:
			print(cover_board(0,0,board))
		test_case -= 1

if __name__ == '__main__':
	main()