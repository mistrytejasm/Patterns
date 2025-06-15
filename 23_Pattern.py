# Pascal's Triangle Pattern in Python

# Enter the row size for the pattern: 5
#           1   
#         1   1   
#       1   2   1   
#     1   3   3   1   
#   1   4   6   4   1   

# pending to solve
n = 5

for i in range(n):
  num = 1
  for j in range(n-i):
    print(" ", end=" ")
  for k in range(i+1):
    print(num, end=" ")
    num = num * (i-k) // (k+1)
  print()