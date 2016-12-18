# -*- coding: utf-8 -*-

rows = []
rounds = 40

trap = ["^^.", ".^^", "^..", "..^"]

def main():
	inp = open("in18.txt").read()[:-1]
	#inp = "..^^."

	rlen = len(inp)
	rows.append(inp)
	res = inp.count(".")

	for row in range(rounds-1):
		newrow = ""
		for idx in range(rlen):
			if idx == 0:
				check = "." + rows[row][:2]
			elif idx == rlen -1:
				check = rows[row][idx-1:idx+1] + "."
			else:
				check = rows[row][idx-1:idx+2]

			if check in trap:
				newrow += "^"
			else:
				res +=1
				newrow += "."

		rows.append(newrow)

	print(res)


if __name__ == '__main__':
	main()
