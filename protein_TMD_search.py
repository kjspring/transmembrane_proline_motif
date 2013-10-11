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
filename = "/Users/kspring/repositories/transmembrane_proline_motif/test_data.fasta"

# Open and parse the sequence data file and index them as a dictionary
data_dict = SeqIO.index(filename, "fasta")
#print record_dict["tr|L7IFC2|L7IFC2_MAGOY"] #use any record ID from the test data


# Open the data file and save it as a list
handle = open(filename, "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()

# Make an index of the hydrophobicity scales
hp_index = {'I':  4.5, 'V':  4.2, 'L':  3.8,
	    'P':  2.8, 'C':  2.5, 'M':  1.9,
	    'A':  1.8, 'G': -0.4, 'T': -0.7,
	    'S': -0.8, 'W': -0.9, 'P': -1.6,
	    'H': -3.2, 'E': -3.5, 'Q': -3.5,
	    'A': -3.5, 'N': -3.5, 'K': -3.9,
	    'R': -4.5, 'Y': -1.3} 	       # A list of tuples
					       # of Kyte & Doolittle 
					       # (kd) hydrophobicity scale 
					       # hyrophobic aa's are negative
# Sample code
def my_hp_search(records):
	hp_seq = [(aa, hp_index[aa]) for aa in records[aa].seq
	return hp_seq


# http://telliott99.blogspot.com/2010/03/kyte-doolittle-hydrophobicity-plot-in.html

X.protein_scale(hp_index, 20, 1.0) #(dict scale, window, edge)


