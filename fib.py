import sys

n = int(sys.argv[1])
k = int(sys.argv[2])

f1 = 1
f2 = 1

for i in range(2, n):
	f = f1 + k * f2
	f2 = f1
	f1 = f

print f