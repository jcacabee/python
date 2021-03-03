from myMath import myArithmetic,myCalcArea,myStatistics

def myAdd(x, y,z,a,b):
    return x + y+z+a+b

def myMean( A):
  sum = 0
  N = 0
  for i in A:
    sum += i
    N += 1
  if N > 0:
    return sum/N
  if N == 0:
    return False

arr = [1, 1, 1, 2]

print(myStatistics.myMean(arr))
