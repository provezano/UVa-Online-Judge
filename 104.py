import sys

def print_path(s, t, l, succ):
	if l == 0:
		print(s+1)
	else:
		print(s+1, end=" ")
		print_path(succ[s][t][l],t,l-1,succ)

def floyd(n, data, path, dist):
	for s in range(2,n+1):
		for i in range(n):
			for j in range(n):
				for k in range(n):
					if dist[i][j][s] < float(data[i][k]) * dist[k][j][s-1]:
						dist[i][j][s] = float(data[i][k]) * dist[k][j][s-1]
						path[i][j][s] = k

						if dist[i][i][s] >= 1.01:
							print_path(i, i, s, path)
							return
	print("no arbitrage sequence exists");


if __name__ == "__main__":
	v = 20
	
	for line in sys.stdin:
		n = int(line.rstrip())
	
		data = []

		for _ in range(n):
			data.append(sys.stdin.readline().rstrip().split())

		for i in range(0,n):
			data[i].insert(i, 1.0)

		dist = [[[0]*v for i in range(v)] for j in range(v)]
		path = [[[0]*v for i in range(v)] for j in range(v)]

		for i in range(n):
			for j in range(n):
				if i == j:
					dist[i][j][1] = 1.0
				else:
					dist[i][j][1] = float(data[i][j])
				if float(data[i][j]) > 0:
					path[i][j][1] = j

		floyd(n, data, path, dist)
	#print()
