n1 = int(raw_input('Please enter number #1: '))
n2 = int(raw_input('Please enter number #2: '))

def peasant(x, y):
	yl = []
	while x > 1:
		x = x // 2
		y = y * 2
		if x % 2 != 0:
			yl.append(y)
		print(y)
	print('The result of the multiplication: %d' % sum(yl))

peasant(n1, n2)	
