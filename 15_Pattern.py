# Inverted Number Pyramid Pattern in Python

# Enter the row size for the pattern: 5
# 1 2 3 4 5 4 3 2 1 
#   1 2 3 4 3 2 1 
#     1 2 3 2 1 
#       1 2 1 
#         1 

n = int(input("Enter Number of Rows: "))

for i in range(n,0, -1):
  for j in range(n-i):
    print(" ", end=" ")
  for k in range(1, i + 1):
    print(k, end=" ")
  for l in range(i-1, 0, -1):
    print(l, end=" ")
  print()