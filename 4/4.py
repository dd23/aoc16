# -*- coding: utf-8 -*-

import re
import operator


def decrypt(ct, num):
	num = num % 26
	res = ""
	for c in ct:
		if c == "-":
			res += "-"
		else:
			res += chr(((ord(c) - 97 + num) % 26) + 97)
	return res


def checksum(name):
	freqs = {}
	name.strip("-")
	for ltr in range(ord('a'), ord('z')+1):
		freqs[chr(ltr)] = name.count(chr(ltr))

	cs = sorted(freqs.items(), key=operator.itemgetter(0)) # sort alphabetically
	cs = sorted(cs, key=operator.itemgetter(1), reverse=True) # sort descending by number
	cs = list(map(lambda x: x[0], cs))[:5]

	return(''.join(cs))


def part1():
	idsum = 0
	for rl in open("in4.txt"):
		rm = re.match("(.*)-(\d+)\[(.*)\]", rl)
		name, idnum, cs = rm.group(1), int(rm.group(2)), rm.group(3)
	
		if cs == checksum(name):
			idsum += idnum
	print("sum:", idsum)
	

def part2():
	for rl in open("in4.txt"):
		rm = re.match("(.*)-(\d+)\[(.*)\]", rl)
		name, idnum, cs = rm.group(1), int(rm.group(2)), rm.group(3)
	
		if cs == checksum(name):
			dname = decrypt(name, idnum)
			if "pole" in dname:
				print(dname, idnum)


def main():
	part1()
	part2()


if __name__ == '__main__':
	main()
