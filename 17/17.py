# -*- coding: utf-8 -*-

import hashlib

ok = ["b", "c", "d", "e", "f"]
inp = "qtetzkpl".encode('ascii')
plens, paths = [], []


def recs(posx, posy, path):
	if posx == posy == 3:
		plens.append(len(path))
		paths.append(path)
		return

	h = hashlib.md5(inp + path.encode('ascii')).hexdigest()

	if h[0] in ok and posy > 0:
		recs(posx, posy - 1, path + "U")
	if h[1] in ok and posy < 3:
		recs(posx, posy + 1, path + "D")
	if h[2] in ok and posx > 0:
		recs(posx - 1, posy, path + "L")
	if h[3] in ok and posx < 3:
		recs(posx + 1, posy, path + "R")

	return


def main():
	path = ""
	posx, posy = 0, 0

	recs(posx, posy, path)

	print("Part1:", min(plens), paths[plens.index(min(plens))])
	print("Part2:", max(plens), paths[plens.index(max(plens))])

if __name__ == '__main__':
	main()

