# find label distribution of stanford treebank sets

if __name__ == "__main__":
	data_file = "data/treebank-train.txt"

	count0 = 0
	count1 = 0
	count2 = 0
	count3 = 0
	count4 = 0

	with open(data_file) as file:
		for line in file:
			lab = int(line[1])

			if lab == 0:
				count0 += 1
			elif lab == 1:
				count1 += 1
			elif lab == 2:
				count2 += 1
			elif lab == 3:
				count3 += 1
			elif lab == 4:
				count4 += 1

	print "0s:", count0
	print "1s:", count1
	print "2s:", count2
	print "3s:", count3
	print "4s:", count4

	print count0+count1+count2+count3+count4
