import sys

number=int(sys.argv[1])

if (number % 2) == 0:
  print "Even"
elif (number % 2) == 1:
  print "Odd"
else:
  print "Is this a number????"