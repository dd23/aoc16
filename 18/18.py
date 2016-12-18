# -*- coding: utf-8 -*-

import re

rounds = 40

def main():
	inp = open("in18.txt").read()[:-1]
	#inp = "..^^."

	rlen = len(inp)
	rows = inp
	res = inp.count(".")

	for row in range(rounds-1):
		newrow = ""
		for idx in range(rlen):
			if idx == 0:
				check = "." != rows[1]
			elif idx == rlen -1:
				check = rows[idx-1] != "."
			else:
				check = rows[idx-1] != rows[idx+1]

			if check:
				newrow += "^"
			else:
				res +=1
				newrow += "."

		rows = newrow

	print(res)

def tt():
	s = "^^."
	rm = re.match(r"(.)\1(?!\1).|(.)((?!\2).)\3", s)
	print(rm)


if __name__ == '__main__':
	main()
	#tt()