#take an input DNA sequence
#and create a dictionary containing the base counts
#Valid bases are:
#(GATC)
#e.g.: {'G': 5, 'A': 3} ...
#extra credit: compute the GC-content of the sequence
#GC content = the proportion of bases that are either G or C (number from 0 to 1)
#extra credit 2: write a script that works for *either* DNA or RNA sequences, depending on the input
#RNA valid bases: GAUC


import sys

sequence=sys.argv[1]

dna_dict={}
total=0
for base in sequence:
  total=total+1
  if dna_dict.has_key(base):
    count= dna_dict[base]
    new_count = count +1
    dna_dict[base]=new_count
  else:
    dna_dict[base]=1
    
print dna_dict

print  ((dna_dict["G"] + dna_dict["C"])/float(total)*100)