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

f_path = abspath("1.016_345.fasta")

# Open the data file and save it as a list
handle = open(f_path, "rU")
records = list(SeqIO.parse(handle, "fasta", IUPAC.extended_protein))
handle.close()
count = len(records)

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

li = []
for i in range(0,count):
    search = re.search(regex01, str(records[i].seq))
    if search != None:
        print records[i]
        li.append(records[i])
    print i


# Output

# Search for the palindrome

li2 = []
regex02 = "G[^P].*?P"
for i in range(0,count):
    search = re.search(regex02, str(records[i].seq))
    if search != None:
        print records[i]
        li2.append(records[i])
    print i

# combine the lists
tot_li = [li, li2]

# for each list and
# for each item in the list;
# write the item to the file, with a hard return
f = open('motifData.csv', 'w')
regex03 = "\\|(.*?)\\|"
url = "http://www.uniprot.org/uniprot/"
stringA = '|'
for list in tot_li:
    n = 0
    for item in list:
        name = re.search(regex03, str(list[n].id))
        f.write(name.group(1))
        #print(name.group(1))
        f.write(',')
        #print (',')
        f.write(str(list[n].seq))
        #print(list[n].seq)
        f.write(',')
        #print(',')
        url2 = url + str(name.group(1))
        f.write(url2)
        #print(url2)
        f.write('\n')
        #print('\n')
        n = n + 1

f.close()


# For XML data

xml_path = abspath("1.016_a.xml")

handle = open(xml_path, "rU")
xml_rec = list(SeqIO.parse(handle, "uniprot-xml", IUPAC.extended_protein))
handle.close()
