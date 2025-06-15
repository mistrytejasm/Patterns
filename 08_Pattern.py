# Hollow Inverted Right-Angled Triangle Pattern in Python

# Enter the row size for the pattern: 4
# * * * * 
# *   * 
# * * 
# * 

n = int(input("Enter Number of Rows : "))

for i in range(n, 0, -1):
  for j in range(1, n+1):
    if j == 1 or i == n or i == j:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print() 