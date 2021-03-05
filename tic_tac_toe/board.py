"""
The board which tac tac toe is played upon.
"""

import pprint

class Board:
	"""
	The board which tac tac toe is played upon.
	"""

	def __init__(self):
		"""
		Initialize an empty board.
		"""

		self.board = [
						[None, None, None],
						[None, None, None],
						[None, None, None]
		]

	def game_over(self):
		"""
		Determine whether or not the game is over.

		Returns:
			False : indicates the game is not over
			True : indicates the game is over and has ended in a draw
			'X' : indicates the 'X' player has won
			'O' : indicates the 'O' player has won
		"""
		"""
		row  = 3
		column = 3
		
		Fill_Counter = 0
		
		for x in range(row):
			for y in range(column):
				if self.board[x][y] != "None":
					Fill_Counter += 1
				if Right_Check(insert parameters) == True or Down_Check(param) == True or Diagonal_Right(param) == True or Diagonal_Left(param) == True:
					if Check_Symbol == 'X':
						return 'X'
					
					if(Check_Symbol == 'O':
						return 'O'
				
			if Fill_Counter == 9:
				return True
		
		return False
		"""
		pass
	
	def Right_Check(self, x, y, row, col):
		for i in range(3):
			if x < 0 or x > row or y < 0 or y + i >= col:	
				return False;
			if self.board[x][y + i] != 'X' and self.board[x][y + i] != 'O':
				return False
			if self.board[x][y + i] == 'X':
				return 'X'
			if self.board[x][y + i] == 'O':
				return 'O'
		 return None
	
	def Down_Check(self, x, y, row, col):
		for i in range(3):
			if x + i < 0 or x + i >= row or y < 0 or y > col:	
				return False;
			if self.board[x + i][y] != 'X' and self.board[x][y + i] != 'O':
			if self.board[x + i][y] == 'X':
				return 'X'
			if self.board[x + i][y] == 'O':
				return 'O'
			
		 return None
	
	def Diagonal_Left(self, x, y, row, col):
		for i in range(3):
			if x + i < 0 or x + i >= row or y - i < 0 or y - i >= col:	
				return False;
			if self.board[x + i][y - i] != 'X' and self.board[x + i][y - i] != 'O':
				if self.board[x + i][y - i] == 'X': 
					return 'X'
				if self.board[x + i][y - i] == 'O':
					return 'O'
		 return None
	
	def Diagonal_Right(self, x, y, row, col):
		for i in range(3):
			if x + i < 0 or x + i >= row or y + i < 0 or y + i >= col:	
				return False;
			if self.board[x + i][y + i] != 'X' and self.board[x + i][y + i] != 'O':
			if self.board[x + i][y + i] == 'X': 
				return 'X'
			if self.board[x + i][y + i] == 'O':
				return 'O'
		 return None
		
	
		

	@staticmethod
	def number_of_features():
		"""
		Return the number of features in the target representation.
		"""

		return 10

	def target_representation(self, positive_board_piece):
		"""
		Return the features, x_0, x_1,...x_10 for the current board.

		Notes: the representation assigns a numerical value to each of
			the nine squares. The value is x_i = 1 if the player has a
			piece in square i, x_i = 0 if square i is empty, and 
			x_i = -1 if the opponent has a piece is square i. The x_i
			represents the square value of square i, such that the
			squares are labelled 1, 2, 3, ..., 9 from top left to bottom
			right.

		Arguments:
			positive_board_piece : the piece that a player moves with,
				either 'X', or 'O'

		Returns:
			list of feature values
		"""

		x = [None for i in range(self.number_of_features())]
		x[0] = 1
		for row in self.board:
			for square in row:
				if square is None:
					x.append(0)
				elif square == positive_board_piece:
					x.append(1)
				else:
					x.append(-1)

		return x

def tests():

	board = Board()

	weights = [0, 1, 1, 1, 1, 10, 1, 1, 1, 1]
	board.board = [
		['X', 'X', 'O'],
		['X', 'O', None],
		[None, None, None]
	]
	print("Should value the middle piece highly: ")
	print("Board: ")
	pprint.pprint(board.board)
	print("'X' score:", board.target_representation(weights, 'X'))
	print("'O' score:", board.target_representation(weights, 'O'))

	weights = [0, 10, 1, 10, 1, 1, 1, 10, 1, 10]
	board.board = [
		['X', 'O', 'X'],
		['O', 'O', None],
		[None, None, None]
	]
	print("Should value the corner pieces highly: ")
	print("Board: ")
	pprint.pprint(board.board)
	print("'X' score:", board.target_representation(weights, 'X'))
	print("'O' score:", board.target_representation(weights, 'O'))

if __name__ == "__main__":
	tests()
