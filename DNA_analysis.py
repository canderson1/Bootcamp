from DNAsequence import DNASequence
from DNAsequence import RNASequence

seq="GATCTAGTGATGCAC"
Rseq="GACUUCGACCAGU"

my_seq = DNASequence(seq) #remeber to initiate the class
my_RNA = RNASequence(Rseq)

print my_seq.gc_content()
print my_seq.reverse_complement()
print my_RNA.reverse_complement()
print my_seq.base_count("A")