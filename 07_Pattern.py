# Hollow Right-Angled Triangle Pattern in Python

# Enter the row size for the pattern: 5
# * 
# * * 
# *   * 
# *     * 
# * * * * * 

n = int(input("Enter Number OF Rows: "))

for i in range(1,  n+1):
  for j in range(1, i+1):
    if i == n or j == 1 or j == i:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()