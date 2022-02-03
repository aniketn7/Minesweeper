from random import randint

class Cell(object): 
	
	def __init__(self): 
		self.isMine = False
		self.isFlagged = False
		self.display = '-'
		self.value = 0
		self.revealed = False
	
	
	
	def flag(self):
		self.isFlagged = True
		self.display = '@'
		
		
		
	def change_display(self, new_display): 
		self.display = new_display
		
		

class Grid(object): 
	
	def __init__(self, side_length): 
		self.side_length = side_length
		self.game_grid = []
		
		for i in range(0, self.side_length): 
			row = []
			
			for j in range(0, self.side_length): 
				currCell = Cell()
				row.append(currCell)
			
			self.game_grid.append(row)
			
		self.numMines = int(0.20 * self.side_length ** 2)
		
		
		
	def populate_mines(self, start_row, start_col): 
		mines_set = 0
		
		while mines_set < self.numMines: 
			row = randint(0, self.side_length - 1)
			col = randint(0, self.side_length - 1)
			
			if row != start_row or col != start_col: 
				if self.is_around(start_row, start_col, row, col) == False: 
					if self.game_grid[row][col].isMine == False: 
						self.game_grid[row][col].isMine = True
						self.game_grid[row][col].value = -1
						mines_set += 1
				
		for i in range(0, self.side_length): 
			
			for j in range(0, self.side_length): 
				if self.game_grid[i][j].isMine == False: 
					self.game_grid[i][j].value = self.evaluate_values(i, j)
	
	
	
	def is_around(self, r1, c1, r2, c2): 
		if r1 == 0:
			
			if c1 == 0: 
				if r2 == r1 and c2 == c1 + 1: 
					return True
				if r2 == r1 + 1 and c2 == c1: 
					return True
				if r2 == r1 + 1 and c2 == c1 + 1: 
					return True
			
			elif c1 == self.side_length - 1: 	
				if r2 == r1 and c2 == c1 - 1: 
					return True
				if r2 == r1 + 1 and c2 == c1 - 1: 
					return True
				if r2 == r1 + 1 and c2 == c1: 
					return True
				
			else: 
				if r2 == r1 and c2 == c1 - 1: 
					return True
				if r2 == r1 + 1 and c2 == c1 - 1: 
					return True
				if r2 == r1 + 1 and c2 == c1: 
					return True
				if r2 == r1 + 1 and c2 == c1 + 1: 
					return True
				if r2 == r1 and c2 == c1 + 1: 
					return True
					
		elif r1 == self.side_length - 1: 
		
			if c1 == 0: 
				if r2 == r1 - 1 and c2 == c1: 
					return True
				if r2 == r1 - 1 and c2 == c1 + 1: 
					return True
				if r2 == r1 and c2 == c1 + 1: 
					return True
			
			elif c1 == self.side_length - 1: 
				if r2 == r1 - 1 and c2 == c1: 
					return True
				if r2 == r1 - 1 and c2 == c1 - 1: 
					return True
				if r2 == r1 and c2 == c1 - 1: 
					return True
			
			else: 
				if r2 == r1 and c2 == c1 - 1: 
					return True
				if r2 == r1 - 1 and c2 == c1 - 1: 
					return True
				if r2 == r1 - 1 and c2 == c1: 
					return True
				if r2 == r1 - 1 and c2 == c1 + 1: 
					return True
				if r2 == r1 and c2 == c1 + 1: 
					return True
					
		elif c1 == 0: 
			
			if r2 == r1 - 1 and c2 == c1: 
				return True
			if r2 == r1 - 1 and c2 == c1 + 1: 
				return True
			if r2 == r1 and c2 == c1 + 1: 
				return True
			if r2 == r1 + 1 and c2 == c1 + 1: 
				return True
			if r2 == r1 + 1 and c2 == c1: 
				return True
			
		elif c1 == self.side_length - 1: 
			
			if r2 == r1 - 1 and c2 == c1: 
				return True
			if r2 == r1 - 1 and c2 == c1 - 1: 
				return True
			if r2 == r1 and c2 == c1 - 1: 
				return True
			if r2 == r1 + 1 and c2 == c1 - 1: 
				return True
			if r2 == r1 + 1 and c2 == c1: 
				return True
				
		else: 
			
			if r2 == r1 and c2 == c1 - 1: 
				return True
			if r2 == r1 - 1 and c2 == c1 - 1: 
				return True
			if r2 == r1 - 1 and c2 == c1: 
				return True
			if r2 == r1 - 1 and c2 == c1 + 1: 
				return True
			if r2 == r1 and c2 == c1 + 1: 
				return True
			if r2 == r1 + 1 and c2 == c1 + 1: 
				return True
			if r2 == r1 + 1 and c2 == c1: 
				return True
			if r2 == r1 + 1 and c2 == c1 - 1: 
				return True
				
		return False		
				
				
	def evaluate_values(self, row, col): 
		value = 0
		
		if row == 0:
			
			if col == 0: 
				if self.game_grid[row][col + 1].isMine == True: 
					value += 1
				if self.game_grid[row + 1][col].isMine == True: 
					value += 1
				if self.game_grid[row + 1][col + 1] == True: 
					value += 1
			
			elif col == self.side_length - 1: 	
				if self.game_grid[row][col - 1].isMine == True: 
					value += 1
				if self.game_grid[row + 1][col - 1].isMine == True: 
					value += 1
				if self.game_grid[row + 1][col].isMine == True: 
					value += 1
				
			else: 
				if self.game_grid[row][col - 1].isMine == True: 
					value += 1
				if self.game_grid[row + 1][col - 1].isMine == True: 
					value += 1
				if self.game_grid[row + 1][col].isMine == True: 
					value += 1
				if self.game_grid[row + 1][col + 1].isMine == True: 
					value += 1
				if self.game_grid[row][col + 1].isMine == True: 
					value += 1
					
		elif row == self.side_length - 1: 
		
			if col == 0: 
				if self.game_grid[row - 1][col].isMine == True: 
					value += 1
				if self.game_grid[row - 1][col + 1].isMine == True: 
					value += 1
				if self.game_grid[row][col + 1].isMine == True: 
					value += 1
			
			elif col == self.side_length - 1: 
				if self.game_grid[row - 1][col].isMine == True: 
					value += 1
				if self.game_grid[row - 1][col - 1].isMine == True: 
					value += 1
				if self.game_grid[row][col - 1].isMine == True: 
					value += 1
			
			else: 
				if self.game_grid[row][col - 1].isMine == True: 
					value += 1
				if self.game_grid[row - 1][col - 1].isMine == True: 
					value += 1
				if self.game_grid[row - 1][col].isMine == True: 
					value += 1
				if self.game_grid[row - 1][col + 1].isMine == True: 
					value += 1
				if self.game_grid[row][col + 1].isMine == True: 
					value += 1
					
		elif col == 0: 
			
			if self.game_grid[row - 1][col].isMine == True: 
				value += 1
			if self.game_grid[row - 1][col + 1].isMine == True: 
				value += 1
			if self.game_grid[row][col + 1].isMine == True: 
				value += 1
			if self.game_grid[row + 1][col + 1].isMine == True: 
				value += 1
			if self.game_grid[row + 1][col].isMine == True: 
				value += 1
			
		elif col == self.side_length - 1: 
			
			if self.game_grid[row - 1][col].isMine == True: 
				value += 1
			if self.game_grid[row - 1][col - 1].isMine == True: 
				value += 1
			if self.game_grid[row][col - 1].isMine == True: 
				value += 1
			if self.game_grid[row + 1][col - 1].isMine == True: 
				value += 1
			if self.game_grid[row + 1][col].isMine == True: 
				value += 1
				
		else: 
			
			if self.game_grid[row][col - 1].isMine == True: 
				value += 1
			if self.game_grid[row - 1][col - 1].isMine == True: 
				value += 1
			if self.game_grid[row - 1][col].isMine == True: 
				value += 1
			if self.game_grid[row - 1][col + 1].isMine == True: 
				value += 1
			if self.game_grid[row][col + 1].isMine == True: 
				value += 1
			if self.game_grid[row + 1][col + 1].isMine == True: 
				value += 1
			if self.game_grid[row + 1][col].isMine == True: 
				value += 1
			if self.game_grid[row + 1][col - 1].isMine == True: 
				value += 1
		
		self.game_grid[row][col].value = value
	
	
	
	def around_mine(self, row, col):
		if row == 0:
			
			if col == 0: 
				if self.game_grid[row][col + 1].isMine == True: 
					return True
				if self.game_grid[row + 1][col].isMine == True: 
					return True
				if self.game_grid[row + 1][col + 1] == True: 
					return True
			
			elif col == self.side_length - 1: 	
				if self.game_grid[row][col - 1].isMine == True: 
					return True
				if self.game_grid[row + 1][col - 1].isMine == True: 
					return True
				if self.game_grid[row + 1][col].isMine == True: 
					return True
				
			else: 
				if self.game_grid[row][col - 1].isMine == True: 
					return True
				if self.game_grid[row + 1][col - 1].isMine == True: 
					return True
				if self.game_grid[row + 1][col].isMine == True: 
					return True
				if self.game_grid[row + 1][col + 1].isMine == True: 
					return True
				if self.game_grid[row][col + 1].isMine == True: 
					return True
					
		elif row == self.side_length - 1: 
		
			if col == 0: 
				if self.game_grid[row - 1][col].isMine == True: 
					return True
				if self.game_grid[row - 1][col + 1].isMine == True: 
					return True
				if self.game_grid[row][col + 1].isMine == True: 
					return True
			
			elif col == self.side_length - 1: 
				if self.game_grid[row - 1][col].isMine == True: 
					return True
				if self.game_grid[row - 1][col - 1].isMine == True: 
					return True
				if self.game_grid[row][col - 1].isMine == True: 
					return True
			
			else: 
				if self.game_grid[row][col - 1].isMine == True: 
					return True
				if self.game_grid[row - 1][col - 1].isMine == True: 
					return True
				if self.game_grid[row - 1][col].isMine == True: 
					return True
				if self.game_grid[row - 1][col + 1].isMine == True: 
					return True
				if self.game_grid[row][col + 1].isMine == True: 
					return True
					
		elif col == 0: 
			
			if self.game_grid[row - 1][col].isMine == True: 
				return True
			if self.game_grid[row - 1][col + 1].isMine == True: 
				return True
			if self.game_grid[row][col + 1].isMine == True: 
				return True
			if self.game_grid[row + 1][col + 1].isMine == True: 
				return True
			if self.game_grid[row + 1][col].isMine == True: 
				return True
			
		elif col == self.side_length - 1: 
			
			if self.game_grid[row - 1][col].isMine == True: 
				return True
			if self.game_grid[row - 1][col - 1].isMine == True: 
				return True
			if self.game_grid[row][col - 1].isMine == True: 
				return True
			if self.game_grid[row + 1][col - 1].isMine == True: 
				return True
			if self.game_grid[row + 1][col].isMine == True: 
				return True
				
		else: 
			
			if self.game_grid[row][col - 1].isMine == True: 
				return True
			if self.game_grid[row - 1][col - 1].isMine == True: 
				return True
			if self.game_grid[row - 1][col].isMine == True: 
				return True
			if self.game_grid[row - 1][col + 1].isMine == True: 
				return True
			if self.game_grid[row][col + 1].isMine == True: 
				return True
			if self.game_grid[row + 1][col + 1].isMine == True: 
				return True
			if self.game_grid[row + 1][col].isMine == True: 
				return True
			if self.game_grid[row + 1][col - 1].isMine == True: 
				return True
		
		return False
	
	
	
	def display_grid(self): 
		for i in range(0, self.side_length): 
			
			for j in range(0, self.side_length): 
				print self.game_grid[i][j].display, " ", 
			print "\n"
		
		print "------------------------------------------------------------------------\n"
	
	 
		
		
			











# grid = Grid(10)
# print grid.numMines
# cell = Cell()
# print cell.display
# grid.game_grid[0][0] = cell
# for i in range(0, grid.side_length): 
	# for j in range(0, grid.side_length): 
		# print grid.game_grid[i][j].display,
	# print "\n"
			
		