#!/usr/bin/python3
import os
import pandas as pd
import numpy as np
# Navigate directory to exercise folder
os.chdir('/localdisk/home/s2903949/exercises/lecture17')
# Read eukaryotes file as dataframe
df = pd.read_csv('eukaryotes.txt',sep='\t',na_values =['-'])

# Question 1
# Filter for fungi
df_fungi = df[df['Group']=='Fungi']
# Filter for large fungi genomes
df_LargeFungi = df_fungi[df_fungi['Size (Mb)']>100]
# Export to csv
df_LargeFungi.to_csv('LargeFungi.txt',sep = '\t',header=True)

# Question 2
# Count on Group
df_Kingdoms=df['Group'].value_counts()
# Export to csv
df_Kingdoms.to_csv('KingdomCounts.txt',sep = '\t',header=True)

# Question 3
# Filter Organism if contains Heliconius
df_Heliconius = df[df['#Organism/Name'].str.contains('Heliconius')]
Heliconius = set(df_Heliconius['#Organism/Name'])
print("The full set is" + str(Heliconius))

# Question 4
# Filter for plants
df_Plants = df[df['Group']=='Plants']
# Take head of value counts on Center
PlantCenter = df_Plants['Center'].value_counts().head(1)
# Filter for insects
df_Insects = df[df['SubGroup']=='Insects']
# Take head of value counts on Center
InsectCenter = df_Insects['Center'].value_counts().head(1)
print("The center with the most plant genomes is %s abd the center with the most insect genomes is %s"%(PlantCenter,InsectCenter))

# Question 5
# Create new coluns with proteins per gene
df['Proteins/Genes'] = df['Proteins']/df['Genes']
df_HighProt = df[df['Proteins/Genes']>1.1]
df_HighProt.to_csv('HighProtein.txt',sep = '\t',header=True)