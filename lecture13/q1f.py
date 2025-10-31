#!/usr/bin/python3
import os

# Change directory and read file, files have already been copied
os.chdir("/localdisk/home/s2903949/exercises/lecture13")
input = open("input.txt").read()

# Split input file on new line file (default)
input = input.split()

# Create length list with same size as input
# Open output file
out = open("q1Output.txt","w")

for i in range (0,len(input)):
	# Trim off the first 14 nucleotides from each string
	input[i] = input[i][13:]
	out.write(input[i]+"\n")
	# Report length to screen
	print(len(input[i]))
out.close()