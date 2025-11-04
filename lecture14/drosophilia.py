#!/usr/bin/python3

# Import packages
import os
# Import data from csv file
with open('data.csv') as data:
  table = data.read()
# Split on the new line character
table = table.split('\n')
try:
  # Iterate across each line
  for i in range (0,len(table)):
    # Split again on commas to form information
    sub = table[i].split(',')
    # Check if the species is one of the selected ones
    if sub[0] == 'Drosophila melanogaster' or sub[0] == 'Drosophila simulans':
      # Print the gene name for the line
      print(sub[2]+"gene belongs to D. melanogaster or D. simulans")
    # Check if gene length is between 90 and 110 bases
    if len(sub[1])>= 90 and len(sub[1])<= 110:
      print(sub[2]+"gene is between 90 and 110 bases long")
    # Calculate AT percentage for each gene
    AT = sub[1].count('a') + sub[1].count('t')
    Per = AT/ len(sub[1])
    # Check if gene has AT percentage under 0,5 and has expression above 200
    if Per < 0.5 and int(sub[3])>200:
      print (sub[2]+ "gene has less than 0.5 AT and expression is greater than 200")
    # Check if gene starts with k or h and belongs to Drosophilia melanogaster
    if (sub[2].startswith('k') or sub[2].startswith('h')) and sub[0]=='Drosophila melanogaster':
      print(sub[2]+"gene starts with k or h and belongs to Drosophilia melanogaster")
    # if elif block to check the AT content of the gene
    if Per < 0.5:
      print (sub[2] +"has a low AT content")
    elif Per >0.65:
      print(sub[2]+"has a high AT content")
    else:
      print(sub[2]+"has a medium AT content")
except:
  print("Line is not parseable")