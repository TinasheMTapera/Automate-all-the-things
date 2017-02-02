#! /usr/bin/python

import sys
import re

print(str(sys.argv[1]))
myfile = open(sys.argv[1], "r")
output = open("output.csv","w")

for line in myfile:
	currentLine = line
	currentLine = re.sub("[ \t]+",",",currentLine)
	currentLine = re.sub(",{4}",",",currentLine)
	cells = currentLine.split(",")
	uselessColumns = [5,10]
	newline = ",".join([cells[i] for i in range(len(cells)) if i not in uselessColumns])
	output.write(newline)

myfile.close()
output.close()
