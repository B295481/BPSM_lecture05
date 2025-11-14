#!/usr/bin/python3
import re
acc = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for i in acc:
  # Contains the number 5
  if re.search('5', i):
    print("%s contains the number 5"%(i))
  # Contains the letter d or e
  if re.search(r'd|e', i):
    print("%s contains d or e"%(i))
    # contains teh letters de in that order
  if re.search(r'd.*e', i):
    print("%s contains de in that order"%(i))
    # Contains de with a single letter between them
  if re.search(r'd.e', i):
    print("%s contains de with a single letter between them"%(i))
    # Contains d and e in any order
  if re.search('d', i) and re.search('e', i):
    print("%s contains de in any order"%(i))
    # Starts with x or y
  if re.search(r'^[xy]', i):
    print("%s starts with x or y"%(i))
    # stats with x or y and ends with e
  if re.search(r'^[xy]', i) and re.search(r'e$', i):
    print("%s starts with x or y and ends in e"%(i))
    # Contains 3 numbers in any order
  if len(re.findall(r'\d',i))==3:
    print("%s contains 3 numbers in any order"%(i))
    # Contains 3 different numbers in the accession
  if len(set(re.findall(r'\d',i)))==3:
    print("%s contains 3 unique numbers in any order"%(i))
    # Contains three or more numbers in a row
  if re.search(r'\d{3,}',i):
    print("%s contains 3 or more numbers in a row"%(i))
    # Ends with d followed by a,r or p
  if re.search(r'd[arp]$',i):
    print("%s contains 3 or more numbers in a row"%(i))