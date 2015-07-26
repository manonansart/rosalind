# http://rosalind.info/problems/gc/

from __future__ import division

f = open('rosalind_gc.txt', 'r')

names = []
dnas = []
gcs = []
dna = ""

for line in f:
    if line[0] == ">":
        names.append(line[1:-1])
        if dna != "":
            dnas.append(dna)
            dna = ""
    else:
        if line[-1] == "\n":
            dna = dna + line[0:-1]
        else:
            dna = dna + line
        
dnas.append(dna)

for dna in dnas:
    gc = 0
    for c in dna:
        if (c == "C") | (c == "G"):
            gc = gc + 1
    gcs.append(gc/len(dna) * 100)
    
inds = [i for i, j in enumerate(gcs) if j == max(gcs)]

for ind in inds:
    print names[ind]
    print gcs[ind]