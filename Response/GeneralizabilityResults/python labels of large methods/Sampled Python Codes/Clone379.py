def opener(file) :
	letters = string.ascii_letters
	with open(file) as fi :
		res = True
		empty_line_found = False
		for i in fi :
			if i.strip() :
				if empty_line_found :
					return False
				if any(j not in letters for j in i.strip().split(':') [0]) :
					return False
			else :
				empty_line_found = True
	return res


def opener(file) :
	fi = open(file).read().splitlines()
	import string
	res = True
	for i in fi :
		if any(j not in string.ascii_letters for j in i.split(':') [0]) :
			res = False
		else :
			continue
	return res

