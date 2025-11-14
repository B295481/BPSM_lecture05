seq = open('/localdisk/data/BPSM/Lecture18/long_dna.txt').read().rstrip('\n') 
cuts = []
num = 0
BpsmI = 'A[GATC]TAAT'
BpsmII = 'GC[AG][AT]TG'

for i in re.finditer(BpsmI, seq): 
  cuts.append(i.start() + 3) 
for i in re.finditer(BpsmII, seq): 
  cuts.append(i.start() + 4)
cuts.sort()
cut = 0
count = 0
for position in cuts:
  counter = counter + 1
  frag = position - cut
  print('Fragment number %s is %s long and ranges from %s to %s'%(counter,frag, cut, position))
  cut = position