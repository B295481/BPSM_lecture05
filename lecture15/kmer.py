def kmer(sequence, kmersize, frequency=3):
  # Force sequence to all uppercase
  sequence = sequence.upper()
  # Initialize variable list
  kmers = []
  # For loop to iterate over sliding window
  for i in range (0,len(sequence)-kmersize):
    # Append kmer to list each time
    kmer.append(sequence[i:i+kmersize])
  # Reduce to set of kmers
  kset = set(kmer)
  ret = []
  for i in range (0,len(kset)):
    ct = kmer.count(kset[i])
    if ct >= frequency:
      ret.append(kset[i])
  return ret