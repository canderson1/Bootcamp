from rodents import Rodent
rodents = {}

file=open('rodent.txt', 'r')

for line in file:
  a,b = line.strip().split(',')
#  print a
#  print b
  if rodents.has_key(a):
    rodents[a].add_weight(b)
  else:
    my_rodent = Rodent(a)
    my_rodent.add_weight(b)
    rodents[a]= my_rodent
    
print rodents
for i in rodents:
  print rodents[i].tag_id, rodents[i].weights
