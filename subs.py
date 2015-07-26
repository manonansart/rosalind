# http://rosalind.info/problems/subs/

f = open('rosalind_subs.txt', 'r')

def cleanLine(line):
    if line[-1] == "\n":
        return line[0:-1]
    else:
        return line

lines = f.readlines()
s = cleanLine(lines[0])
substr = cleanLine(lines[1])
indexes = []

for i in range(0, len(s)):
    if s[i:i+len(substr)] == substr:
        indexes.append(i + 1)


        
print ' '.join(str(ind) for ind in indexes)