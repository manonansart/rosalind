# http://rosalind.info/problems/hamm/

f = open('rosalind_hamm.txt', 'r')

def cleanLine(line):
    if line[-1] == "\n":
        return line[0:-1]
    else:
        return line

lines = f.readlines()
dna1 = cleanLine(lines[0])
dna2 = cleanLine(lines[1])

hamm = 0

for i in range(0, len(dna1)):
    if dna1[i] != dna2[i]:
        hamm += 1
        
print hamm