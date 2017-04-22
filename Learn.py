import numpy as np

#positive = +1
#negative = -2
#vicotry = +2

#0 = North
#1 = East
#2 = West
#3 = South

curr = [0,0]	
step = 0
alpha = 0.5
gamma = 0.85
SIZE = 3

def updateQTableCost(curr):
	x = curr[0]
	y = curr[1]

	cost0 = 0
	cost1 = 0
	cost2 = 0
	cost3 = 0

	for i in range(4):

		#NORTH
		if i == 0:
			reward = 0
			if y + 1 > SIZE - 1:
				reward = -2
			elif x == SIZE and y+1 == SIZE:
				reward = 2
			else:
				reward = 1
			cost0 = alpha * (grid[x][y] + gamma * grid[x][y+1] + reward)

		#EAST
		elif i == 1:
			reward = 0
			if x + 1 > SIZE - 1:
				reward = -2
			elif x + 1 == SIZE and y == SIZE:
				reward = 2
			else:
				reward = 1
			cost1 = alpha * (grid[x][y] + gamma * grid[x+1][y] + reward)

		#WEST
		elif i == 2:
			reward = 0
			if x - 1 < 0:
				reward = -2
			elif x - 1 == SIZE and y == SIZE:
				reward = 2
			else:
				reward = 1
			cost2 = alpha * (grid[x][y] + gamma * grid[x-1][y] + reward)

		#SOUTH
		elif i == 3:
			reward = 0
			if y - 1 < 0:
				reward = -2
			elif x == SIZE and y - 1 == SIZE:
				reward = 2
			else:
				reward = 1
			cost3 = alpha * (grid[x][y] + gamma * grid[x][y-1] + reward)

		temp_list = [cost0,cost1,cost2,cost3] 
		cost = max(temp_list)
		index = temp_list.index(cost)

	grid[x][y] = cost
	step += 1
	return index



'''def getNextDirection(curr):
	x = curr[0]
	y = curr[1]
	temp = qTable[x][y]

	#get maximum value from the list
	maxi = max(temp)

	if grid[x][y] < maxi:
		grid[x][y] = maxi

	temp = list(temp)
	index = temp.index(max(temp))

	step += 1
	return [index,maxi]'''


grid = np.zeros(shape=(SIZE, SIZE))
qTable = np.zeros(shape=(SIZE, SIZE, 4))

#will tell where to got and return a ma element. 
direction = updateQTableCost(curr)

#Update the value of the current based on the direction
if index == 0:
	curr[1] += 1
elif index == 1:
	curr[0] += 1
elif index == 2:
	curr[0] -= 1
else:
	curr[1] -= 1

