# Inverted Pyramid Pattern in Python  

# Enter the row size for the pattern: 5
      
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

n = int(input("Enter Row Number: "))

for i in range(n,0, -1):
  for j in range(n-i):
    print(" ", end=" ")
  for k in range(1, 2 * i):
    print("*", end= " ")
  print()