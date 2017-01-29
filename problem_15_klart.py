

from numpy import *

size = 20

grid = zeros([size + 1, size + 1], dtype=long)

def routes(x, y):
	if grid[x, y] == 0:
		if x < size and y < size:
			grid[x, y] = routes(x + 1, y) + routes(x, y + 1)
		elif x < size:
			grid[x, y] = routes(x + 1, y)
		elif y < size:
			grid[x, y] = routes(x, y + 1)
		else:
			grid[x, y] = 1
	return grid[x, y]
		
if __name__ == '__main__':
	
	print routes(0, 0)
	#print grid
