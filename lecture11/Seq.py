ShortSequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# Count the numbers of A and Ts
CountA = ShortSequence.count("A")
CountT = ShortSequence.count("T")
print("There are %s As in the sequence and %s Ts in the sequence"%(CountA,CountT))
CountAT = CountA + CountT
# Calculate the percent AT in this sequence and print it
ATPercent = CountAT/len(ShortSequence)*100
print("There is %s percent AT in this sequence"%(ATPercent))

# Complement DNA
# Initialize complement value
Complement = ""
# Use for loop to go through each posiition and replace values
for i in range(0, len(ShortSequence)):
	if ShortSequence[i] == "A":
		Complement=Complement+"T"
	elif ShortSequence[i] == "T":
		Complement=Complement+"A"
	elif ShortSequence[i] == "C":
		Complement=Complement+"G"
	elif ShortSequence[i] == "G":
		Complement=Complement+"C"
print("The complement is %s"%(Complement))

ShortSequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
# Restriction Fragment Length
RecognitionSite = "GAATTC"
Position = ShortSequence.find(RecognitionSite) + 1
CutPosition = Position + 1
print("The position of the motif is %s, and the cut position is %s"%(Position, CutPosition))

# Find position 2
if ShortSequence.find(RecognitionSite,CutPosition) == -1:
	frag1 = CutPosition + 1
	frag2 = len(ShortSequence) - CutPosition
	print("Only one cut is made, fragment lengths are %s and %s"%(frag1, frag2))
else:
	print("More than one fragement I'm too lazy")

# Introns
ShortBlock = """ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"""
# Create exon slices
Exon1 = ShortBlock[:62]
Exon2 = ShortBlock[90:]
CodingSequence = Exon1 + Exon2
print("The coding sequence is %s"%(CodingSequence))

# Length of coding sequences
CodingLength = len(CodingSequence)
TotalLength = len(ShortBlock)

Percent = CodingLength/TotalLength*100
print("The coding length is %s, and it makes up %s percent of the sequence"%(CodingLength,Percent))

Intron1 = ShortBlock[63:89].lower()
FullSequence = Exon1 + Intron1 + Exon2
print(FullSequence)