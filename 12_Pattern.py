# Number Right-Angled Triangle Pattern in Python

# Enter the row size for the pattern: 4
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4

n = int(input("Enter Number OF Raw: "))

for i in range(1, n+1):
  for j in range(1, i+1):
    print(i, end=" ")
  print()