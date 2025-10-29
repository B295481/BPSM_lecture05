#!/usr/bin/python3
# Read in sequence data for first sequence
with open("plain_genomic_seq.txt") as seq1:
	content1 = seq1.read()
	seq1.close()
# Write information for coding sequences into one file
out1 = open("CD1.fasta","w")
out1.write(seq1[:62].upper())
out1.close()
# Write information for noncoding sequences into another file
out2 = open("NC1.fasta","w")
out2.write(seq1[63:].upper())
out.close()

with open("remote_genome.txt") as seq2:
	content2 = seq2.read()
	seq2.close()
# Write information for coding sequences into one file
out1 = open("CD2.fasta","w")
out1.write(seq2[28:408].upper())
out1.close()
# Write information for noncoding sequences into another file
out2 = open("NC2.fasta","w")
out2.write(seq2[:27].upper())
out.close()
# Open again as an append to include second half
out2 = open("NC2.fasta","a")
out2.write(seq2[409:].upper())
out2.close()