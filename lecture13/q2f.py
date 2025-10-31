#!/usr/bin/python3
import os

# Change directory and read file, files have already been copied
os.chdir("/localdisk/home/s2903949/exercises/lecture13")
dna = open("genomic_dna2.txt").read()
# Strip new line from file
dna = dna.rstrip('\n')

exons = open("exons.txt").read()
# Split on new line
exons = exons.split()
# Create blank list for exons
new = []
# Iterate across exons
for i in range(0,len(exons)):
  # Split each 
  # print(exons[i])
  exon_single = exons[i].split(',')
  # print(exon_single)
  new.append(dna[int(exon_single[0])-1:int(exon_single[1])-1])
# Join individual exon parts from list
complete = ''.join(new)
# Write output into new file
out = open("q2Output.txt","w")
out.write(complete)
out.close()