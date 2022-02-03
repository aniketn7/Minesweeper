import sys
from structure import *

# sys.setrecursionlimit(50)

class Game(object): 
	
	def __innit__(self): 	
		self.rounds = 0
		
		
	def new_game(self): 		
		grid_size = int(raw_input("Enter size of grid: "))
		grid = Grid(grid_size)
		grid.display_grid()
		starting_row = int(raw_input("Choose row: "))
		starting_col = int(raw_input("Choose column: "))
		
		while (starting_row < 0 or starting_row >= grid.side_length) or (starting_col < 0 or starting_col >= grid.side_length): 
			print "Invalid choice. Choose again."
			starting_row = int(raw_input("Choose row: "))
			starting_col = int(raw_input("Choose column: "))
		
		grid.populate_mines(starting_row, starting_col)
		
		for i in range(0, grid.side_length): 
		
			for j in range(0, grid.side_length): 
				grid.evaluate_values(i, j)
		
		self.recursive_reveal_cell(starting_row, starting_col, grid)
		grid.display_grid()
		self.game_loop(grid)
		
		
		
	def game_loop(self, grid): 
		dead = False
		
		while dead == False: 
			decision = raw_input("Enter 'flag', 'reveal', or 'unflag': ")
			
			while decision != 'flag' and decision != 'reveal' and decision != 'unflag': 
				print "Invalid choice. Choose again."
				decision = raw_input("Enter 'flag', 'reveal', or 'unflag': ")
			
			row = int(raw_input("Choose row: "))
			col = int(raw_input("Choose column: "))
			
			while (row < 0 or row >= grid.side_length) or (col < 0 or col >= grid.side_length): 
				print "Invalid choice. Choose again."
				row = int(raw_input("Choose row: "))
				col = int(raw_input("Choose column: "))
			
			if decision == 'flag': 
				if grid.game_grid[row][col].revealed == True: 
					print "Cannot flag something that has already been revealed. Choose again."
				elif grid.game_grid[row][col].isFlagged == True: 
					print "This cell has already been flagged. Choose again."
				else: 
					grid.game_grid[row][col].flag()
			elif decision == 'unflag': 
				if grid.game_grid[row][col].revealed == True: 
					print "Cannot unflag something that has already been revealed. Choose again."
				elif grid.game_grid[row][col].isFlagged == False: 
					print "Cannot unflag something that is not flagged. Choose again."
				else: 
					grid.game_grid[row][col].isFlagged = False
					grid.game_grid[row][col].display = '-'
			elif decision == 'reveal': 
				if grid.game_grid[row][col].revealed == True:
					print "This cell has already been revealed. Choose again."
				elif grid.game_grid[row][col].isFlagged == True: 
					print "Must first unflag before revealing. Choose again."
				else: 
					if grid.game_grid[row][col].value == 0: 
						self.recursive_reveal_cell(row, col, grid)
					else: 
						self.reveal_cell(row, col, grid)
					
			grid.display_grid()
			
			if (grid.game_grid[row][col].isMine == True) and (grid.game_grid[row][col].revealed == True): 
				dead = True
				self.end_game()
					
	
		
	
	def reveal_cell(self, row, col, grid): 
		
		if grid.game_grid[row][col].isMine == True: 
			grid.game_grid[row][col].change_display("*")
			# grid.game_grid[row][col].isMine = True
		elif grid.game_grid[row][col].value == 0: 
			grid.game_grid[row][col].change_display("o")
		else: 
			grid.game_grid[row][col].change_display(str(grid.game_grid[row][col].value))
			
		grid.game_grid[row][col].revealed = True
		
		
	
	def recursive_reveal_cell(self, row, col, grid): 
		self.reveal_cell(row, col, grid)
		
		if grid.around_mine(row, col) == False: 
			
			if col - 1 >= 0: 
				if grid.game_grid[row][col - 1].revealed == False:
					self.recursive_reveal_cell(row, col - 1, grid)
				if row - 1 >= 0: 
					if grid.game_grid[row - 1][col - 1].revealed == False:
						self.recursive_reveal_cell(row - 1, col - 1, grid)
			if row - 1 >= 0: 
				if grid.game_grid[row - 1][col].revealed == False:
					self.recursive_reveal_cell(row - 1, col, grid)
				if col + 1 <= grid.side_length - 1: 
					if grid.game_grid[row - 1][col + 1].revealed == False:
						self.recursive_reveal_cell(row - 1, col + 1, grid)
			if col + 1 <= grid.side_length - 1: 
				if grid.game_grid[row][col + 1].revealed == False:
					self.recursive_reveal_cell(row, col + 1, grid)
				if row + 1 <= grid.side_length - 1:
					if grid.game_grid[row + 1][col + 1].revealed == False:
						self.recursive_reveal_cell(row + 1, col + 1, grid)
			if row + 1 <= grid.side_length - 1: 
				if grid.game_grid[row + 1][col].revealed == False:
					self.recursive_reveal_cell(row + 1, col, grid)
				if col - 1 >= 0: 
					if grid.game_grid[row + 1][col - 1].revealed == False:
						self.recursive_reveal_cell(row + 1, col - 1, grid)
						
						
	
	def end_game(self): 
		print "You selected a mine and died. Better luck next time."
		decision = raw_input("Play again? Enter 'yes' or 'no': ")
		
		if decision == 'yes': 
			self.new_game()
			
			
			