# Hollow Inverted Pyramid Pattern in Python

# Enter the row size for the pattern: 5
# * * * * * * * * * 
#   *           * 
#     *       * 
#       *   * 
#         * 

n = int(input("Enter Number OF Rows: "))

for i in range(n,0, -1):
  for j in range(n-i):
    print(" ", end=" ")
  for k in range(1, 2*i):
    if k == 1 or k == 2*i-1 or i == n:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()