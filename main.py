# Given n = 3 as input, print the following pattern A

n = 3
for i in range(1, n+1):
  for j in range(0, i):
    print("A ", end="")
  print("\r")