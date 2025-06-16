# Cross Pattern in Python

# Enter the row size for the pattern: 5
# *       * 
#   *   *   
#     *     
#   *   *   
# *       * 

n = 5

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j or i+j == n+1:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()
