#!/usr/bin/python

############################################
# Title: search.py
# Purpose: Load up the data and search the transmembrane sequences
# Author: Kevin Spring
# Date: October 11, 2013
############################################

from Bio import SeqIO
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from os.path import abspath
import re

# Load the data

f_path = abspath("1.016_aTESTDATA.fasta")

# Open the data file and save it as a list
handle = open(f_path, "rU")
records = list(SeqIO.parse(handle, "fasta", IUPAC.extended_protein))
handle.close()

# Amino Acid Alphabet
# B = "Asx";  Aspartic acid (R) or Asparagine (N) 
# X = "Xxx";  Unknown or 'other' amino acid 
# Z = "Glx";  Glutamic acid (E) or Glutamine (Q) 
# J = "Xle";  Leucine (L) or Isoleucine (I), used in mass-spec (NMR) 
# U = "Sec";  Selenocysteine 
# O = "Pyl";  Pyrrolysine 

# Search these extracted sequences for the motif
# Regular expressions
#P.*?G
# ? usually means optional, but as * is a quantifier (0 or more) ? acts upon it to make it lazy.
## there must be a proline followed by any hydrophobic, helix forming amino acids, followed by a glycine, or palidromic.

#regex = "P..*?G"
# want it ot be palindromic so maybe "P.*?G | G.*?P"
#regex = "P.*?G | G.*?P"
# don't want a PG result so use P^G.*?G
regex01 = "P[^G].*?G"
regex = "[PG]"
for e in records:
    search = re.search(regex01, str(e.seq))
    if search != None:
        print e

# Search for the palindrome

regex02 = "G[^P].*?P"
for e in records:
    search = re.search(regex02, str(e.seq))
    if search != None:
        print e

    
