#given a string which is a sentence "Apple, banana, and cherry."
#find out how many unique letters A-Z that sentence contains
#(capital and lower case should not be double counted!)

#extra credit: given *two* sentences, find out how many letters
#they have in common (A-Z) and how many letters are unique
#to each sentences

import sys
import string
sentence1=sys.argv[1]
sentence2=sys.argv[2]



sentence1=set(sentence1.lower())
sentence2=set(sentence2.lower())
sentence_union=sentence1.union(sentence2)
#print sentence_union
alphabet = set(string.lowercase)
#print alphabet
print "That sentence 1 had " + str(len(set(alphabet.intersection(set(sentence1))))) + " unique characters."
print "That sentence 2 had " + str(len(set(alphabet.intersection(set(sentence2))))) + " unique characters."
print "Unique to both sentences there are " + str(len(set(alphabet.intersection(set(sentence_union))))) + " characters."

