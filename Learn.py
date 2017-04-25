import numpy as np
import random
import matplotlib.pyplot as plt

#positive = +1
#negative = -2
#vicotry = +100

#0 = North
#1 = East
#2 = South
#3 = West


curr = [0,0]	
alpha = 0.5
gamma = 0.85
SIZE = 15
grid = np.zeros(shape=(SIZE, SIZE))
qTable = np.zeros(shape=(SIZE, SIZE, 4))
eps = 70
Qcost = 0.0

def takeRandom():
	rand = random.randrange(100)
	if rand >= eps:
		return False #We will not be going random	
	return True #We will be going random

def updateAgent(curr,direction):

	x = curr[0] 
	y = curr[1] 
	my_list = []

	#North
	if direction == 0:
		if x > 0:
			x -= 1
	
	#East
	if direction == 1:
		if y < SIZE - 1:
			y += 1
	
	#South
	if direction == 2:
		if x < SIZE-1:
			x += 1
	
	#West
	if direction == 3:
		if y > 0:
			y -= 1

	if x == curr[0] and y == curr[0]:
		#We have gone off the edge and returned back to same state
		reward = -2.0
	elif x == SIZE-1 and y == SIZE-1:
		#We have reached the goal 
		reward = 100.0
	else:
		#Have moved to correct location
		reward = 1.0

	next = [x,y]
	my_list.append(reward)
	my_list.append(next)
	return my_list


def updateQTable(reward,next_location,curr,direction):

	global Qcost
	x = next_location[0]
	y = next_location[1]
	a = curr[0]
	b = curr[1]

	Qcost = qTable[a][b][direction] + alpha * (reward + gamma * max(qTable[x][y]) - qTable[a][b][direction])
	qTable[a][b][direction] = Qcost
	
	return Qcost


if __name__ == "__main__":
	
	next_location = [0,0]
	cnt = 0
	direction = 0
	cnt_list = []
	range_list = range(1000)
	for i in range(1000):	
		flag = True
		
		curr = [0,0]
		cnt = 0
		while(flag):
			#print('-------------------curr-----------------------', curr)
			x = curr[0]
			y = curr[1]

			if x == SIZE-1 and y == SIZE-1:
				flag = False
				print('-------------------cnt-----------------------', cnt)
				cnt_list.append(cnt)
				if i == 1000:
					plt.plot(cnt_list,range_list)
					plt.show()
				break
			else:
				cnt += 1
				
			#Decide if we should go random or not
			random_flag = takeRandom()

			#Decide the direction
			if(random_flag):
				direction = random.randrange(4)
			else:
				maxi = max(qTable[x][y])
				indexes = [i for i, j in enumerate(qTable[x][y]) if j == maxi]
				if len(indexes) == 1:
					direction = indexes[0]
				else:
					direction = random.choice(indexes)

			direction_list = updateAgent(curr,direction)
			reward = direction_list[0]
			next_location = direction_list[1]
			#Direction will have [reward,next_location]

			QCost = updateQTable(reward,next_location,curr,direction)

			curr = next_location