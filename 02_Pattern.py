# Inverted Right-Angled Triangle in Python

# Enter the row size for the pattern: 5

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

n = int(input("Enter the Row Number: "))

for i in range(n,0, -1):
  for j in range(1, i+1):
    print("*", end= " ")
  print()