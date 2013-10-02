#write a program that takes a list of three or more words on the command line
#print those words, in alphabetical order, separated by commas, with the final word preceded by "and" and a period at the end
#e.g. python my_program.py apple strawberry banana cherry
#apple, banana, cherry, and strawberry.
#bonus: capitalize the first letter of the sentence

import sys

my_list=sys.argv[1:] # get list of inputs from the command line minus the name of the script
my_list.sort() # sort the list
sentence = ', '.join(my_list[:-1]) + " and " + my_list[-1] + "." #join all the words in the list but the last and and then the last word and a full stop.
print sentence[0].upper() + sentence[1:] # Capitalise the first letter note can also use title() or capitalize()
