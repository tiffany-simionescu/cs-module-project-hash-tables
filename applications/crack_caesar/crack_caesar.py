# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here             
from collections import Counter

frequency_order = [
    'E', 'T', 'A', 'O', 'H', 'N', 
    'R', 'I', 'S', 'D', 'L', 'W', 
    'U', 'G', 'F', 'B', 'M', 'Y', 
    'C', 'P', 'K', 'V', 'Q', 'J', 
    'X', 'Z'
    ]

def crack_caesar():

  with open("applications/crack_caesar/ciphertext.txt") as f:
      content = f.read()

  alpha_count = Counter(filter(str.isalnum, content))
  cache = {k:v for (k,v) in zip([i[0] for i in alpha_count.most_common()], frequency_order)}
  output = ""

  for char in content:
      output_char =  char
      if char in cache.keys():
          output_char = cache[char]
      output += output_char
  
  return output

if __name__ == "__main__":
      print(crack_caesar()) 