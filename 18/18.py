# -*- coding: utf-8 -*-

rounds = 40 #part 1
#rounds = 400000 #part 2

def main():
	inp = open("in18.txt").read()[:-1]
	rlen = len(inp) - 1
	row = inp
	res = inp.count(".")

	for _ in range(rounds - 1):
		newrow = row[1]
		for idx in range(1, rlen): # skip first and last idx
			newrow += "^" if row[idx-1] != row[idx+1] else "."
		row = newrow + row[-2]
		res += row.count(".")# this is faster than +1 for every non-trap idx

	print(res)


if __name__ == '__main__':
	main()
