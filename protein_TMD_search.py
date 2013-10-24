#!/usr/bin/python

############################################
# Title: protein_TMD_search.py
# Purpose: Find area of proteins to search
# Author: Kevin Spring
# Date: October 11, 2013
############################################

from Bio import SeqIO
from Bio import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Test data filename
filename = "/Users/kspring/repositories/transmembrane_proline_motif/testData02.fasta"

# Open and parse the sequence data file and index them as a dictionary
data_dict = SeqIO.index(filename, "fasta")
#print record_dict["tr|L7IFC2|L7IFC2_MAGOY"] #use any record ID from the test data


# Open the data file and save it as a list
handle = open(filename, "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()

#to print a specific list item seq do records[i].seq

# Kyte & Doolittle index of hydrophobicity
kd_index = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
    'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
    'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
    'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }
# A list of tuples
# of Kyte & Doolittle 
# (kd) hydrophobicity scale 
# hyrophobic aa's are negative

# Convert the amino acid sequence to the Kyte & Doolittle hydrophobicity index scale
# code is modified from http://www.dalkescientific.com/writings/NBN/plotting.html
values = []
#for e in record:
#    for residue in e.seq:
#        values.append(kd_index[residue]) # need to find a way to make a list within a list


# Sample code
def my_hp_search(records):
    
window = 20
for e in records:
    #i = 0
    size = len(e.seq)
    for i in range(size):
        #i = 0
        kd_value = []
        seq_scan = e.seq[i:i+(window - 1)]
    # need to be able to get to the last of the a.a. sequence.  The current problem is that the sequences are not in multiples of 20 so there is some left over.
        print i + 1
        print seq_scan
        for residue in seq_scan:
            kd_value.append(kd_index[residue])
        kd = sum(kd_value) # dictionary mapping of a.a. to kd index
        print kd
    print e.seq
    print size

# Next look for regions that are next to each other that have a kd value below 0 and have that whole length annotated as a hydrophobic region.  The only important values are where the first a.a. is located when the mean kd < 0 and the a.a. location of the residue before it is > 0.
                
print records[5].seq        
        
# see the function nt_search in Bio.SeqUtils

# http://telliott99.blogspot.com/2010/03/kyte-doolittle-hydrophobicity-plot-in.html

X.protein_scale(hp_index, 20, 1.0) #(dict scale, window, edge)

# Transmembrane is a derived class of BioPhython's Seq class with the added variables of where the transmembrane domains exist and how many there are.
class Transmembrane(Seq):
    <statement-1>
    <statement-2>
    #a Function that determines how many transmembrane domains or passes through the 
