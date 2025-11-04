def amino(sequence, acid):
  try:
    acid = acid.upper()
    length=len(sequence)
    sub = sequence.count(acid)
    frac = (sub/length)*100
    return frac
  except:
    return"Error in arguments"
def aminos(sequence, acid= ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
  try:
    acid = acid.upper()
    length = len(sequence)
    counter = 0
    for i in range(0,len(acid)):
      sub = sequence.count(acid[i])
      counter = sub + counter
    frac = (counter/length)*100
    return frac
  except:
    return"Error in arguments"
def nonstandard(sequence, threshold = 0.2):
  counter = 0 
  for i in range (0,len(sequence)):
    if sequence[i] not in ['A','T','C','G']:
      counter = counter + 1
  final = counter/ len(sequence)
  if final> threshold:
    return "High"
  else:
    return "Low"