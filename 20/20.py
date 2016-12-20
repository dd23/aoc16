# -*- coding: utf-8 -*-

def main():
	nums = {}
	for line in open("in20.txt"):
		line = line.split("-")
		nums[int(line[0])] = int(line[1])

	compacted = {}
	nmin, nmax = 0, 0
	iprange = (0, 2**32 - 1)
	freeip = min(sorted(nums)) - iprange[0] # number of free ips from iprange to smallest blocked


	#merge overlapping or adjacent blocks of blocked ips
	for n in sorted(nums):
		nmin = min(n, nmin)
		if n <= nmax + 1: # +1 for adjacent
			nmax = max(nmax, nums[n])
		else:
			freeip += n - nmax - 1 # -1, since boarders are not included
			compacted[nmin] = nmax # merged block
			nmin = n
			nmax = nums[n]

	freeip += iprange[1] - nmax # free ips from max blocked to end of ip range

	print("Part1:", compacted[0] + 1) # solution 1 is the free IP right after the first block
	print("Part2:", freeip)


if __name__ == '__main__':
	main()
