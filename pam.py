import math
import sys
import random
import matplotlib.pyplot as plt


def d(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def readFile(k, file):

	file = open(file, 'r')
	
	x = []
	y = []

	for line in file:
		a, b = line.split()
		x.append(float(a))
		y.append(float(b))


	return x, y

def createMedoids(x, y, k):

	mx = []
	my = []	
	
	for i in range(0, k):
		a = random.randint(0, len(x))
		mx.append(x[a])
		my.append(y[a])

	#pontos começam em um cluster aleatório 
	c = []
	for i in range(0, len(x)):
		c.append(random.randint(0, k-1))

	return c, mx, my


def updateCluster(x, y, c, mx, my, k):

	for i in range(0, len(c)): #todos os pontos
		m = float('inf')
		for j in range(0, k): #todos os medoides
			distance = d(x[i], y[i], mx[j], my[j])
			if distance < m:
				# print(i, d(x[i], y[i], cx[j], cy[j]), j)
				m = distance
				c[i] = j
	return c

def calCost(x, y, c, mx, my, k):

	cost = 0.0
	for i in range(0, k):
		costMedoid = 0.0
		for j in range(len(c)):
			if c[j] == i:
				costMedoid += d(mx[i], my[i], x[j], y[j])
		cost += costMedoid

	return cost

def main():

	file  = sys.argv[1]
	k = int(sys.argv[2])

	x, y = readFile(k, file)

	c, mx, my = createMedoids(x, y, k)

	c = updateCluster(x, y, c, mx, my, k)

	allowableLossCost = 10
	
	while allowableLossCost > 0:
		for i in range(0, k):
			for j in range(0, len(c)):
				if c[j] == i:
					if (mx[i] != x[j]) and (my[i] != y[j]):
						mx_old = mx[i]
						my_old = my[i]
						previousCost = calCost(x, y, c, mx, my, k)
						mx[i] = x[j]
						my[i] = y[j]
						c = updateCluster(x, y, c, mx, my, k)
						newCost = calCost(x, y, c, mx, my, k)

						if previousCost < newCost:
							allowableLossCost -= 1
							mx[i] = mx_old
							my[i] = my_old
							c = updateCluster(x, y, c, mx, my, k)

	colors = ['b', 'g', 'r', 'c', 'm']
	markers = ['o', '^', '1' , 's', '+', '*', 'x']


	for i in range(0, len(c)): # todos os pontos
		for j in range(0, k):	# todos os clusters
			if c[i] == j:
				plt.plot(x[i], y[i], colors[j % len(colors)]+markers[j % len(markers)])

	print(len(mx))
	print(len(my))

	for i in range(0, k): # medoides pontos pretos
		plt.plot(mx[i], my[i], 'ko') 

	plt.title('pam '+sys.argv[1]+'  k='+sys.argv[2])

	plt.show()


if __name__ == '__main__':
	main()