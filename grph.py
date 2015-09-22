# http://rosalind.info/problems/grph/

def cleanLine(line):
    if line[-1] == "\n":
        return line[0:-1]
    else:
        return line

f = open("rosalind_grph.txt", 'r')

k = 3
names = []
lines = []
s = ""
adjency = []

for line in f:
    if line[0] == ">":
        names.append(line[1:-1])
        if s != "":
            lines.append(s)
            s = ""
    else:
        if line[-1] == "\n":
            s = s + line[0:-1]
        else:
            s = s + line

lines.append(s)

for i in range(0, len(lines)):
    suffix = lines[i][-1 * k:len(lines[i])]
    for j in range(0, len(lines)):
        if lines[j][0:k] == suffix:
            if i != j:
                adjency.append(names[i] + ' ' + names[j])

output = open('output.txt', 'w')
output.write('\n'.join(adjency))