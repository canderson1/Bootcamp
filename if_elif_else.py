#Exercise 2: More complex if statements
#Write a python code that accepts a single integer
#if the number is less than 50 and greater than 0 print "Minor"
#if the number is greater than or equal to 50 and less than 1000 print "Major"
#Otherwise prints "Severe"
import sys

number=int(sys.argv[1])

if (number < 50 and number > 0):
  print "minor"
elif (number >= 50 and number < 1000):
  print "major"
else:
  print "severe"