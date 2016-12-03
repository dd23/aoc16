# -*- coding: utf-8 -*-

def isTriangle(rl):
	return rl[0]+rl[1]>rl[2] and rl[0]+rl[2]>rl[1] and rl[2]+rl[1]>rl[0]


def part1():
	count = 0

	with open("in3.txt") as inputfile:
		for rl in inputfile:
			rl=list(map(int, rl.split()))
			count += isTriangle(rl)
	
	print("possible triangles:", count)


def part2():
	count, idx = 0, 0
	ins = []	

	with open("in3.txt") as inputfile:
		for rl in inputfile:
			ins.append(list(map(int, rl.split()))) #store numbers
			idx += 1
			if idx % 3 == 0: #if we have three sets of numbers
				ins = list(map(list, zip(*ins))) #transose inputs
				for el in ins:
					count += isTriangle(el)
				ins.clear()

	print("possible triangles:", count)


def main():
	part1()
	part2()


if __name__ == '__main__':
	main()
