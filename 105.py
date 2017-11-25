import sys

def main():
	height = [0] * 10000
	count = 0

	for line in sys.stdin:
		count += 1
		coord = [int(x) for x in line.split(' ')]
		for i in range(coord[0], coord[2]):
			if coord[1] > height[i]:
				height[i] = coord[1]
		
	c = i = current_height = 0
	first_printed = False
	
	while (i != 10000):
		if height[i] != current_height:
			if not first_printed:
				print("{0} {1}".format(i, height[i]), end="")
				first_printed = True
			else:
				print(" {0} {1}".format(i, height[i]), end="")
			current_height = height[i]
		i += 1
	print("")


if __name__ == "__main__":
    main()
	