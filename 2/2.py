# -*- coding: utf-8 -*-

def part1():
	with open("in2.txt") as inputfile:
		posx = 1
		posy = 1
		code = ''

		for rl in inputfile:
			for char in rl:

				if char == 'D':
					posy = min(posy + 1, 2)
				elif char == 'U':
					posy = max(posy - 1, 0)
				elif char == 'R':
					posx = min(posx + 1, 2)
				elif char == 'L':
					posx = max(posx - 1, 0)

			code += str(3 * posy + posx + 1)

	print(code)


pad2 = ['0','0','1','0','0',
	   '0','2','3','4','0',
	   '5','6','7','8','9',
	   '0','A','B','C','0',
	   '0','0','D','0','0']

def onpad(x, y):
	return (0 <= x < 5 and 0 <= y < 5 and pad2[x + 5*y] != '0')

def part2():
	with open("in2.txt") as inputfile:
		posx = 0
		posy = 2
		code = ''


		for rl in inputfile:
			for char in rl:

				if char == 'D':
					pnew = posy + 1
					if onpad(posx, pnew):
						posy = pnew
				elif char == 'U':
					pnew = posy - 1
					if onpad(posx, pnew):
						posy = pnew
				elif char == 'R':
					pnew = posx + 1
					if onpad(pnew, posy):
						posx = pnew
				elif char == 'L':
					pnew = posx - 1
					if onpad(pnew, posy):
						posx = pnew
				else: # new lines and other crap
					pass

			code += str(pad2[posx + 5*posy])
	print(code)


def main():
	part1()
	part2()


if __name__ == '__main__':
	main()
