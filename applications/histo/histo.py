# Your code here
def histo():
  skip_characters = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
  cache = {}

  with open("applications/histo/robin.txt") as f:
    lowercase_words = f.read().lower().strip(skip_characters).split()

  for word in lowercase_words:
    if word not in cache:
      cache[word] = 1
    else:
      cache[word] += 1

  sort_word_count = sorted(cache.items(), key=lambda item: item[1], reverse=True)
  greatest_num = len(sorted(cache.keys(), key=lambda x: len(x))[-1])

  for k, v in sort_word_count:
    histo = ' ' * (greatest_num - len(k)) + v * '#'
    print(f"{k}  {histo}")

# if __name__ == "__main__":
#     print(histo())

histo()