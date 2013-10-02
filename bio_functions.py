#GATCTAGTGATGCAC

def base_count(sequence, base):
    # returns the number of times base X occurs
    # in the sequence
    return sequence.count(base)

    
def gc_content(sequence):
    # returns the GC content of the sequence
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

  return  ((dna_dict["G"] + dna_dict["C"])/float(total)*100)


if __name__ == "__main__":
  seq="GATCTAGTGATGCAC"
  
  for base in "ATCGUN":
    print "The are " + str(base_count(seq, base)) + " " + base + " in this sequence: " + seq
  print "GC content is " + str(gc_content(seq))