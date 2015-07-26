# http://rosalind.info/problems/iprb/

from __future__ import division
import sys

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

total = k + m + n

print 1 - (n*(n-1)/(total * (total-1)) + (m*n)/(total * (total-1)) + (m*(m -1))/(4 * total * (total-1)))