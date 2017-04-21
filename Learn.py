# Define blank list
board = []
zero_list = [0,0,0,0]

#Generate rows with length of 15
for row in range(15):
  # Append a blank list to each row cell
  board.append([])
  for column in range(15):
    board[row].append(str(initial))


def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)