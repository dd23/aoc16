# -*- coding: utf-8 -*-

import re


def main():
	botvals = {}
	ops = {}
	outs = {}
	for line in open("in10.txt"):
		if line.startswith("value"):
			rm = re.match(r"value (\d+) goes to bot (\d+)", line)
			val, tbot = rm.groups()
			tbot = int(tbot)
			if not tbot in botvals:
				botvals[tbot] = [int(val)]
			else:
				botvals[tbot].append(int(val))

		elif line.startswith("bot"):
			rm = re.match(r"bot (\d+) gives low to ([a-z]+) (\d+) and high to ([a-z]+) (\d+)", line)
			tbot, ltar, low, htar, high = rm.groups()
			tbot = int(tbot)
			if not tbot in ops:
				ops[tbot] = [ltar, int(low), htar, int(high)]


	for it in range(500):

		switch = False

		if 0 in outs and 1 in outs and 2 in outs:
			print("Solution 2:", outs[0]*outs[1]*outs[2])
			return

		for b in ops:
			if b in botvals and len(botvals[b]) == 2:

				if 17 in botvals[b] and 61 in botvals[b]:
					print("Solution 1:", b)

				switch = True
				ltar, low, htar, high = ops[b]
				break

		if switch:

			if ltar == "bot":
				if not low in botvals:
					botvals[low] = [min(botvals[b])]
				else:
					botvals[low].append(min(botvals[b]))
			else:
				outs[low] = min(botvals[b])

			if htar == "bot":
				if not high in botvals:
					botvals[high] = [max(botvals[b])]
				else:
					botvals[high].append(max(botvals[b]))
			else:
				outs[high] = max(botvals[b])

			botvals[b].clear()


if __name__ == '__main__':
	main()
