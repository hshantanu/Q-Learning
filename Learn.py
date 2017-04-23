import numpy as np
import random

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

	print('-------------------curr-----------------------', curr)
	x = curr[0]
	y = curr[1]
	cost = []
	cost0 = 0
	cost1 = 0
	cost2 = 0
	cost3 = 0
	step = 0
	maxi = 0
	flag = True
	for i in range(4):

		
		#NORTH
		flag = True
		if i == 0:
			reward = 0
			if y + 1 > SIZE - 1:
				reward = -2
				flag = False
			elif x == SIZE and y+1 == SIZE:
				reward = 2
				flag = False
			else:
				reward = 1
			print('-------------------flag1-----------------------', flag)
			if (flag == True):
				print "in first"
				cost0 = alpha * (grid[x][y] + gamma * grid[x][y+1] + reward)
			else:
				print "In second"
				cost0 = alpha * (grid[x][y] + gamma * grid[x][y] + reward)
			
			qTable[x][y][0] = cost0
			if cost0 >= maxi:
				maxi = cost0
				cost.append(maxi)

		#EAST
		elif i == 1:
			flag = True
			reward = 0
			if x + 1 > SIZE - 1:
				reward = -2
				flag = False
			elif x + 1 == SIZE and y == SIZE:
				reward = 2
				flag = False
			else:
				reward = 1

			print('-------------------flag-----------------------', flag)
			if (flag == True):
				print "In fisrt"	
				cost1 = alpha * (grid[x][y] + gamma * grid[x+1][y] + reward)
			else:
				print "In second"
				cost1 = alpha * (grid[x][y] + gamma * grid[x][y] + reward)

			qTable[x][y][1] = cost1
			if cost1 > maxi:
				cost.pop()
				maxi = cost1
				cost.append(cost1)
			elif cost1 == maxi:
				cost.append(maxi)

		#WEST
		elif i == 2:
			flag = True
			reward = 0
			if x - 1 < 0:
				reward = -2
				flag = False
			elif x - 1 == SIZE and y == SIZE:
				reward = 2
				flag = False
			else:
				reward = 1

			if (flag == True):
				cost2 = alpha * (grid[x][y] + gamma * grid[x-1][y] + reward)
			else:
				cost2 = alpha * (grid[x][y] + gamma * grid[x][y] + reward)

			qTable[x][y][2] = cost2
			if cost2 > maxi:
				cost.pop()
				maxi = cost2
				cost.append(cost2)
			elif cost2 == maxi:
				cost.append(maxi)

		#SOUTH

		elif i == 3:
			flag = True
			reward = 0
			if y - 1 < 0:
				reward = -2
				flag = False
			elif x == SIZE and y - 1 == SIZE:
				reward = 2
				flag = False
			else:
				reward = 1

			if (flag == True):
				cost3 = alpha * (grid[x][y] + gamma * grid[x][y-1] + reward)
			else:
				cost3 = alpha * (grid[x][y] + gamma * grid[x][y] + reward)

			qTable[x][y][3] = cost3
			if cost3 > maxi:
				cost.pop()
				maxi = cost3
				cost.append(cost3)
			elif cost3 == maxi:
				cost.append(maxi)

		print('-------------------cost-----------------------', cost)
		maxi_cost = max(cost)
		#index = cost.index(maxi_cost)
		index = random.randrange(len(cost))

	grid[x][y] = maxi_cost
	
	step += 1
	return index


grid = np.zeros(shape=(SIZE, SIZE))
qTable = np.zeros(shape=(SIZE, SIZE, 4))
flag = True

while(flag):
	if curr[0] == SIZE-1 and curr[1] == SIZE-1:
		flag = False
		print('-------------------curr-----------------------', curr)
		break
	else:
		#will tell where to got and return a ma element. 
		direction = updateQTableCost(curr)

		#Update the value of the current based on the direction
		if direction == 0:
			if curr[1] < SIZE-1:
				curr[1] += 1
		elif direction == 1:
			if curr[0] < SIZE-1:
				curr[0] += 1
		elif direction == 2:
			if curr[0] > 0:
				curr[0] -= 1
		elif curr[1] > 0:
			curr[1] -= 1
