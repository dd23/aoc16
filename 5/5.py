# -*- coding: utf-8 -*-

import hashlib

puzzleinput = "cxdnnyjw".encode('utf-8')


def part1():
	passwd = ""
	ctr = 0
	while len(passwd) < 8:
		h = hashlib.md5(puzzleinput + str(ctr).encode('utf-8')).hexdigest()
		if h.startswith("00000"):
			passwd += h[5]
		ctr += 1

	print(passwd)


def part2():
	passwd = ['']*8
	ctr = 0
	while '' in passwd:
		h = hashlib.md5(puzzleinput + str(ctr).encode('utf-8')).hexdigest()
		if h.startswith("00000"):
			pos = int(h[5], base=16)
			if pos < len(passwd) and passwd[pos] == '':
				passwd[pos] = h[6]

		ctr += 1

	print(''.join(passwd))


def main():
	part1()
	part2()

if __name__ == '__main__':
	main()
