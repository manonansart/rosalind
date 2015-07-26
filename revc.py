import sys

str = sys.argv[1]
new_str = ""

for c in reversed(str):
	if (c == "A"): new_str = new_str + "T"
	if (c == "C"): new_str = new_str + "G"
	if (c == "T"): new_str = new_str + "A"
	if (c == "G"): new_str = new_str + "C"

print new_str