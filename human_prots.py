#(3) Write a Python script that
#-opens the file
#-reads each line of the file
#-if the first character of the line is a > character AND the protein is a Human one (i..e contains the string "OS=Homo sapiens" then count the number of lines
#-at end , print out the number of human proteins inside SwissProt

file=open('uniprot_sprot.fasta', 'r')
counter=0
pattern='OS=Homo sapiens'
for line in file:
  if line.startswith(">") and pattern in line:
    counter=counter+1
print counter

file.close()