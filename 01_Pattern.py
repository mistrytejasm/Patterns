# https://www.wscubetech.com/resources/python/programs/pattern

# Right-Angled Triangle Pattern in Python

# Enter the row size for the pattern: 5

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

n = int(input("Enter The Row size for The Pattern: "))

for i in range(1,n+1):
  for j in range(1, i+1):
    print("*", end=" ")
  print()