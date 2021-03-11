import sys
import math 
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

def calCentroids(x, y, c, cx, cy, k):

	for i in range(k): #todos os clusters
		a = 0
		sumX = 0.0
		sumY = 0.0
		for j in range(len(c)): #todos os pontos
			if i == c[j]:
				sumX += x[j]
				sumY += y[j]
				a += 1	
		print(i, a)
		if a != 0:	
			cx[i] = sumX/a
			cy[i] = sumY/a

	return cx, cy

def updateCluster(x, y, c, cx, cy, k):

	for i in range(len(c)): #todos os pontos
		m = float('inf')
		for j in range(k): #todos os centroides
			distance = d(x[i], y[i], cx[j], cy[j])
			if distance < m:
				# print(i, d(x[i], y[i], cx[j], cy[j]), j)
				m = distance
				c[i] = j
	return c

def createCentroids(x, y, k):
	
	cx = []
	cy = []	
	
	#centroide começa como algum ponto aleatório
	for i in range(k):
		cx.append(x[random.randint(0, len(x))])
		cy.append(y[random.randint(0, len(y))])

	#pontos começam em um cluster aleatório 
	c = []
	for i in range(len(x)):
		c.append(random.randint(0, k-1))

	return c, cx, cy

def main():

	file  = sys.argv[1]
	k = int(sys.argv[2])
	
	x, y = readFile(k, file)

	c, cx, cy = createCentroids(x, y, k)

	for i in range(50):

		cx, cy = calCentroids(x, y, c, cx, cy, k)

		c = updateCluster(x, y, c, cx, cy, k)


	colors = ['b', 'g', 'r', 'c', 'm']
	markers = ['o', '^', '1' , 's', '+', '*', 'x']


	for i in range(len(c)): # todos os pontos
		for j in range(k):	# todos os clusters
			if c[i] == j:
				plt.plot(x[i], y[i], colors[j % len(colors)]+markers[j % len(markers)])


	for i in range(k): # centroides pontos pretos
		plt.plot(cx[i], cy[i], 'ko') 

	
	plt.title('k-means '+sys.argv[1]+'  k='+sys.argv[2])


	plt.show()

if __name__ == '__main__':
	main()