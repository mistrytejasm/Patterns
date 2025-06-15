# Hollow Butterfly Pattern in Python

# Enter the row size for the pattern: 5
# *                 * 
# * *             * * 
# *   *         *   * 
# *     *     *     * 
# *       * *       * 
# *       * *       * 
# *     *     *     * 
# *   *         *   * 
# * *             * * 
# *                 * 

n = 5

for i in range(1, n+1):
  for j in range(1, i+1):
    if j == 1 or j == i:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  for k in range(2 * (n-i)):
    print(" ", end=" ")
  for l in range(1, i+1):
    if l == 1 or l == i:
      print("*", end= " ")
    else:
      print(" ", end=" ")
  print()

for i in range(n-1, 0, -1):
  for j in range(1, i+1):
    if j == 1 or j == i:
      print("*", end= " ")
    else:
      print(" ", end=" ")
  for k in range(2 * (n-i)):
    print(" ", end=" ")
  for l in range(1, i+1):
    if l == 1 or l == i:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()
