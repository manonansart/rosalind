# http://rosalind.info/problems/cons/

def cleanLine(line):
    if line[-1] == "\n":
        return line[0:-1]
    else:
        return line

f = open("rosalind_cons.txt", 'r')

lines = []
A = []
C = []
G = []
T = []
s = ""

for line in f:
    if line[0] == ">":
        if s != "":
            lines.append(s)
            s = ""
    else:
        if line[-1] == "\n":
            s = s + line[0:-1]
        else:
            s = s + line

lines.append(s)
        
for i in range(0, len(lines[0])):
    A.append(0)
    C.append(0)
    G.append(0)
    T.append(0)
    for line in lines:
        if line[i] == "A": A[-1] = A[-1] + 1
        if line[i] == "C": C[-1] = C[-1] + 1
        if line[i] == "G": G[-1] = G[-1] + 1
        if line[i] == "T": T[-1] = T[-1] + 1

cons = ""

for i in range(0, len(A)):
    counts = [A[i], C[i], G[i], T[i]]
    inds = [i for i, j in enumerate(counts) if j == max(counts)]
    c = ['A', 'C', 'G', 'T'][inds[0]]
    cons = cons + c

output = open('output.txt', 'w')

output.write(cons + '\n')

output.write("A: " + ' '.join(str(n) for n in A) + '\n')
output.write("C: " + ' '.join(str(n) for n in C) + '\n')
output.write("G: " + ' '.join(str(n) for n in G) + '\n')
output.write("T: " + ' '.join(str(n) for n in T) + '\n')