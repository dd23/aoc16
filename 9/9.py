# -*- coding: utf-8 -*-

import re
import time


def part1():
	inp = open("in9.txt").read().strip(" \n\r")
	reslen = 0

	while(True):
		rm = re.match(r"([A-Z]*?)\((\d+)x(\d+)\)", inp)

		if rm:
			add, zlen, times = rm.groups()
			zlen = int(zlen)
			times = int(times)
			inp = inp[len(rm.group(0)) + zlen:] #remove current part
			reslen +=  len(add) + times*zlen
		else:
			reslen += len(inp)
			break

	print(reslen)


def reclen(s):
	if not "(" in s:
		return len(s)
	else:
		rm = re.match(r"([A-Z]*?)\((\d+)x(\d+)\)", s)
		add, zlen, times = rm.groups()
		zlen = int(zlen)
		times = int(times)
		mid = s[len(rm.group(0)):len(rm.group(0))+zlen]
		rest = s[len(rm.group(0)) + zlen : ]
		return len(add) + reclen(mid)*times + reclen(rest)


def part2():
	inp = open("in9.txt").read().strip(" \n\r")
	print(reclen(inp))


def main():
	part1()
	part2()


if __name__ == '__main__':
	main()
