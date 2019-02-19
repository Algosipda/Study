def counting_coverway(blocks_i, blocks_j, row_p, col_p, board):

	if row_p >= len(board):
		return 1
	if col_p >= len(board[row_p]):
		return counting_coverway(blocks_i, blocks_j,row_p+1, 0, board)
	if board[row_p][col_p] == '#':
		return counting_coverway(blocks_i, blocks_j, row_p, col_p + 1, board)
	else:
		res = 0
		for i in range(0, len(blocks_i)):
			if checking_coverable(blocks_i[i], blocks_j[i], row_p, col_p, board):
				res += counting_coverway(blocks_i, blocks_j, row_p, col_p+1, board)
				remove_block(blocks_i[i], blocks_j[i], row_p, col_p, board)

		return res

def checking_coverable(block_i, block_j, row_p, col_p, board):
	coverable = True

	for cell_delta in range(0, len(block_i)):
		if block_i[cell_delta] + row_p < 0 or block_i[cell_delta] + row_p >= len(board):
			coverable = False
			break
		elif block_j[cell_delta] + col_p < 0. or block_j[cell_delta] + col_p >= len(board[row_p]):
			coverable = False
			break
		elif board[row_p + block_i[cell_delta]][col_p + block_j[cell_delta]] == '#':
			coverable = False
			break

	if coverable:
		for cell_delta in range(0, len(block_j)):
			board[row_p + block_i[cell_delta]][col_p + block_j[cell_delta]] = '#'


	return coverable


def remove_block(block_i, block_j, row_p, col_p, board):
	for cell_delta in range(0, len(block_j)):
			board[row_p + block_i[cell_delta]][col_p + block_j[cell_delta]] = '.'


if __name__ == "__main__":
	test_case = int(input())
	blocks_i = [[0, 1, 1], [0, 0, 1], [0, 0, 1], [0, 1, 1]]
	blocks_j = [[0, 0, 1], [0, 1, 1], [0, 1, 0], [0, 0, -1]]

	while test_case > 0:
		board = []
		row, col = map(int, input().split(' '))
		white_space = 0
		for i in range(0, row):
			column = []
			for cell in input():
				if cell == '.':
					white_space += 1
				column.append(cell)
			board.append(column)

		if white_space % 3 !=0:
			print(0)
		else:
			print(counting_coverway(blocks_i, blocks_j, 0, 0, board))

		test_case -= 1


