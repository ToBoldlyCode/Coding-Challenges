import sys

def checksum():
  solution = 0
  for line in sys.stdin:
    row = [int(i) for i in line.split("\t")]
    x = max(row)
    y = min(row)
    solution += x-y
  print(solution)
