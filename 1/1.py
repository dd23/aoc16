# -*- coding: utf-8 -*-

def part1():
	with open("in1.txt") as inputfile:
		rl = inputfile.readline()
		rl = rl.replace(",", "")
		rl = rl.split()

	# 0 = north, 1 = east, 2 = south, 3 = west
	direction = 0
	posx = 0
	posy = 0

	for entry in rl:
		if entry.startswith("R"):
			direction = (direction + 1) % 4
		else: #L
			direction = (direction - 1) % 4
		#print(entry)

		#remove leading L/R and trailing ","
		steps = int(entry[1:])

		if direction == 0:
			posy += steps
		elif direction == 1:
			posx += steps
		elif direction == 2:
			posy -= steps
		else:
			posx -= steps

	# result = "manhattan distance"
	print("Solution 1:", abs(posx) + abs(posy))



def part2():
	with open("in1.txt") as inputfile:
		rl = inputfile.readline()
		rl = rl.replace(",", "")
		rl = rl.split()

	# 0 = north, 1 = east, 2 = south, 3 = west
	direction = 0
	posx = 0
	posy = 0

	# for this problem size a simple list will do. For bigger things, use a bitmap or sth.
	visited = []
	visited.append((posx, posy))

	done = False

	for entry in rl:
		if entry.startswith("R"):
			direction = (direction + 1) % 4
		else: #L
			direction = (direction - 1) % 4
		#print(entry)
		steps = int(entry[1:])


		for i in range(steps):
			if direction == 0:
				posy += 1
			elif direction == 1:
				posx += 1
			elif direction == 2:
				posy -= 1
			else:
				posx -= 1

			if (posx,posy) in visited:
				done = True
				break

			visited.append((posx, posy))

		if done:
			break

	# result = "manhattan distance"
	print("Solution 2:", abs(posx) + abs(posy))
	

def main():
	part1()
	part2()


if __name__ == '__main__':
	main()
