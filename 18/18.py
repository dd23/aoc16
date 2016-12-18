# -*- coding: utf-8 -*-

import re

rounds = 40 #part 1
#rounds = 400000 #part 2

def main():
	inp = open("in18.txt").read()[:-1]

	rlen = len(inp) + 1
	row = inp
	res = inp.count(".")
	row = "." + row + "." # pad with "." to get rid of boundary checks

	for _ in range(rounds - 1):
		newrow = "."
		for idx in range(1, rlen): # rlen is inputlen + 1
			newrow += "^" if row[idx-1] != row[idx+1] else "."
		res += newrow.count(".") - 1 # this is faster than +1 for every non-trap idx
		row = newrow + "." # padding

	print(res)


if __name__ == '__main__':
	main()
