# http://rosalind.info/problems/fibd/

import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

if m == 0:
	print 0

elif m == 1:
	if n == 1:
		print 1
	else:
		print 0

elif n == 1:
	print 1

else:
	f1 = 1
	f2 = 1
	f = 1

	births = [1, 0]

	for i in range(3, n+1):
		if i < m+1:
			f = f1 + f2	
			f2 = f1
			f1 = f
			fm.append(f)
			births.append(f1 - f2)

		else:
			newBirths = sum(births[0:-1])
			births.append(f)
			births.pop(0)

	print sum(births)