# http://rosalind.info/problems/dna/

import sys

str = sys.argv[1]

nbA = 0
nbG = 0
nbC = 0
nbT = 0


for c in str:
    if c == "A": nbA = nbA + 1
    if c == "G": nbG = nbG + 1
    if c == "C": nbC = nbC + 1
    if c == "T": nbT = nbT + 1
        
print nbA, nbC, nbG, nbT