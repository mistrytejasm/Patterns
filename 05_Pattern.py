# Diamond Pattern in Python

# Enter the row size for the pattern: 4

#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
#   * * * * * 
#     * * * 
#       *

n = int(input("Enter Row Number: "))

for i in range(1, n+1):
  for j in range(n-i):
    print(" ", end= " ")
  for k in range(1,2*i):
    print("*", end=" ")
  print()

for i in range(n-1, 0, -1):
  for j in range(n-i):
    print(" ", end=" ")
  for k in range(1, 2 * i):
    print("*", end=" ")
  print()