import random

position = 0
walk = [position]
steps = 1000
for i in xrange(steps):
	step = 1 if random.randint(0, 1) else -1
	position += step
	walk.append(position)
