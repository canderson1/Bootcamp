class Nucleotide_Sequence:
    def __init__(self, sequence):
      assert len(sequence) > 0 #to stop a division of 0 error for gc_content function?
      assert isinstance(sequence, str)
      assert set(sequence).difference(self.valid) == set()
      self.sequence = sequence
      self.base_counts = {}
    
    def base_count(self, base):
      # returns the number of times base X occurs
      # in the sequence and write result to dictionary for us again.

      if base in self.base_counts:
            return self.base_counts[base]
      else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
    
    def gc_content(self):
       # returns the GC content of the sequence
        dna_dict={}
	total=0
	for base in self.sequence:
	  total=total+1
	  if dna_dict.has_key(base):
	    count= dna_dict[base]
	    new_count = count +1
	    dna_dict[base]=new_count
	  else:
	    dna_dict[base]=1
	return  ((dna_dict["G"] + dna_dict["C"])/float(total)*100)
        
    # extra credit
    def reverse_complement(self):
        #rev= self.sequence[::-1]
        #rev = rev.replace("A", "t")
        #rev = rev.replace("T", "a")
        #rev = rev.replace("C", "g")
        #rev = rev.replace("G", "c")
        #rev = rev.replace("U", "a")
        #return rev.upper()
        
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
            
        return rev_c
        
class DNASequence(Nucleotide_Sequence):
    '''Uses the bases GATC.'''
    '''Class appropriate for DNA sequences. Assumes only A,T,C and G are found in the sequence.'''
    complements = {'G': 'C','C': 'G','A': 'T','T': 'A'}
    valid = set(complements.keys()) 
    
class RNASequence(Nucleotide_Sequence):
    '''Uses the bases GAUC.'''
    complements = {'G': 'C', 'C': 'G', 'A': 'U', 'U': 'A'}
    valid = set(complements.keys())
    def __init__(self, sequence):
      Nucleotide_Sequence.__init__(self, sequence)
      assert not 'T' in sequence

