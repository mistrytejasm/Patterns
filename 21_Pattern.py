# Alphabet Diamond Pattern in Python

# Enter the row size for the pattern: 5
#         A 
#       A B A 
#     A B C B A 
#   A B C D C B A 
# A B C D E D C B A 
#   A B C D C B A 
#     A B C B A 
#       A B A 
#         A 

n = 5

for i in range(1, n+1):
  for j in range(n-i):
    print(" ", end=" ")
  for k in range(1, i+1):
    print(chr(64+k), end=" ")
  for l in range(i-1, 0, -1):
    print(chr(64+l), end=" ")
  print()

for i in range(n-1, 0, -1):
  for j in range(n-i):
    print(" ", end=" ")
  for k in range(1, i+1):
    print(chr(64+k), end=" ")
  for l in range(i-1, 0, -1):
    print(chr(64+l), end=" ")
  print()