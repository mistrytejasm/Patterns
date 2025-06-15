import re
import os

def generate_file(base_filename, count):

  # step 1. Extract Number using regex
  match = re.match(r"(\d+)_Pattern\.py",base_filename)
  if not match:
    print("FileName Formate is Incorrect. Use Formate like 04_Pattern.py")
    return
  
  # Step 2. Extract current number and determine padding
  current_num = int(match.group(1))
  padding = len(match.group(1))

  # step 3. Create new file
  for i in range(1, count+1):
    next_num = current_num + i

    new_filename = f"{str(next_num).zfill(padding)}_Pattern.py"

    if not os.path.exists(new_filename):
      with open(new_filename, "w") as f:
        f.write(f"# File: {new_filename}\n")
      print(f"Created: {new_filename}")
    else:
      print(f"Skipped (already Exists): {new_filename}")


generate_file("16_Pattern.py", 9)
