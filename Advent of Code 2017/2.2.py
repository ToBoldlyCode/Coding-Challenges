import sys
import itertools

def checksum2():
  solution = 0
  for line in sys.stdin:
    row = [int(i) for i in line.split("\t")]
    for x,y in itertools.combinations(row,2):
      z=0
      if x%y == 0:
        z = x//y
      elif y%x == 0:
        z = y//x
      solution += z
  print(solution)