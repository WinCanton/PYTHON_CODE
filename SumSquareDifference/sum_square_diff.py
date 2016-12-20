# setup a list containing the first 100 natural numbers
numbers = range(1,101,1)

# calculate the difference
diff = sum(numbers)**2 - sum([x*x for x in numbers])

print diff