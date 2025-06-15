# Alphabet Right-Angled Triangle Pattern in Python

# Enter the row size for the pattern: 5
# A 
# A B 
# A B C 
# A B C D 
# A B C D E

n = 5

for i in range(1, n+1):
  for j in range(1 , i+1):
    print(chr(64 + j), end=" ")
  print()