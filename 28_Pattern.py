# Zig-Zag Number Pattern in Python

# Enter the row size for the pattern: 4
# 1 0 1 0 
# 0 1 0 1 
# 1 0 1 0 
# 0 1 0 1 

n = 4

for i in range(1, n+1):
  for j in range(1, n+1):
    if (i+j) % 2 == 0:
      print("1", end=" ")
    else:
      print("0", end=" ")
  print()