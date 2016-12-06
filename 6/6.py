# -*- coding: utf-8 -*-

import operator




def part1():
	freqs = [{},{},{},{},{},{},{},{}]
	for line in open("in6.txt"):
		for idx in range(8):
			el = line[idx]
			if el in freqs[idx]:
				freqs[idx][el] += 1
			else:
				freqs[idx][el] = 1

	res = ""

	for idx in range(8):
		res += max(freqs[idx].items(), key=operator.itemgetter(1))[0]
	print(res)


def part2():
	freqs = [{},{},{},{},{},{},{},{}]
	for line in open("in6.txt"):
		for idx in range(8):
			el = line[idx]
			if el in freqs[idx]:
				freqs[idx][el] += 1
			else:
				freqs[idx][el] = 1

	res = ""

	for idx in range(8):
		res += min(freqs[idx].items(), key=operator.itemgetter(1))[0]
	print(res)


def main():
	part1()
	part2()

if __name__ == '__main__':
	main()
