# -*- coding: utf-8 -*-

import operator


def part1():
	freqs = [{}, {}, {}, {}, {}, {}, {}, {}] # this looks ugly af but works
	for line in open("in6.txt"):
		for idx in range(8): # count frequencies for each index separately
			el = line[idx]
			if el in freqs[idx]:
				freqs[idx][el] += 1
			else:
				freqs[idx][el] = 1

	res = ""
	for idx in range(8): # find most common element for each index
		res += max(freqs[idx].items(), key=operator.itemgetter(1))[0]
	print(res)


def part2():
	freqs = [{}, {}, {}, {}, {}, {}, {}, {}] # this looks ugly af but works
	for line in open("in6.txt"):
		for idx in range(8): # count frequencies for each index separately
			el = line[idx]
			if el in freqs[idx]:
				freqs[idx][el] += 1
			else:
				freqs[idx][el] = 1

	res = ""
	for idx in range(8): # find least common element for each index
		res += min(freqs[idx].items(), key=operator.itemgetter(1))[0]
	print(res)


def main():
	part1()
	part2()


if __name__ == '__main__':
	main()
