import itertools

i = 0
for pair in itertools.combinations(range(700), 2):
	i+=1
print i