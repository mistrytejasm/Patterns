# Inverted Number Right-Angled Triangle Pattern in Python

# Enter the row size for the pattern: 5
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

n = int(input("Enter Number OF Rows: "))

for i in range(n, 0, -1):
  for j in range(1, i+1):
    print(i, end=" ")
  print()