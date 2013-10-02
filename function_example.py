#functions
import sys
import doctest

def action(n):
  if n == 1:
    return 1
  else:
    return n * action(n-1)

def fib(n):
  assert n>= 0 #using the fib function the input must be a postive integer
  assert isinstance(n, int)
  ''' Doctest expects to see input as it woul;d on the command line followed by the output from the input.
  >>> fib(0)
  0
  >>> fib(1)
  1
  >>> fib(2)
  1
  '''
  if n == 1:
    return 1
  elif n ==2:
    return 1
  else:
    return fib(n-1) + fib(n-2)  #the nth fib number in the sequence is equal to the sum of the previous two! Veryslow
    
def fast_fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b  #multiple assignment avoids using a temporary variable
        n -= 1
    return a

    
if __name__ == "__main__":
  number=int(sys.argv[1])
  print action(number)
  print fib(number)
  print fast_fib(number)
  doctest.testmod()
#  assert fib(0) == 0
#  assert fib(1) == 1
#  assert fib(2) == 1
#  assert fib(3) == 2	#assert statements, a statement that you know is true for test your function is doing what you expect