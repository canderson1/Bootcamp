#Repetition:
#for loop - different from C, Java - arithmetic progression of numbers.
#python for loop iterates over items of any sequence (list or string).
#Exercise: Add the contents of the following list by looping over them

scores = [85.0, 75.0, 95.0, 110.0, 56.0]

total=float(0.0)
for i in scores:
  total = total + i
print total