import random
import re

# Start words are words that begin with a capital, or a `"` followed by a
# capital.

# Stop words are words that end in any of the punctuation `.?!`, or that
# punctuation followed by a `"`.

# Read in all the words in one go
# with open("input.txt") as f:
with open("applications\markov\input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
word_list = words.split()
# Look for character class A-Z at the beginning of the string (^).
# > = if there
start_condition = re.compile('^"?[A-Z]')
# Look for character class .?! at the end of the string ($) 
# and ending with a double quote or possibly a single quote with any charcter before it. 
end_condition = re.compile('[.?!]"?$')

other_condition = '()'.split()

cache = {}

for index, word in enumerate(word_list):
    if word not in cache and word not in other_condition:
        if index + 1 < len(word_list):
            cache[word] = [word_list[index + 1]]
        else:
            cache[word] = [word_list[0]] 
    else:
        if index + 1 < len(word_list):
            cache[word].append(word_list[index + 1])         

# TODO: construct 5 random sentencese
# Your code here
def generator():
    start = False
    stop = False
    starts_with_quotes = False
    ends_with_quotes = False
    key_word = ''
    sentence = ''

    while start == False:
        story = random.choice(list(cache.keys()))
        if start_condition.search(story):
            key_word = story
            if key_word[0] == ' " ':
                starts_with_quotes = True
            else:
                starts_with_quotes = False    
                start = True

    current_word = key_word

    while stop == False:
        if end_condition.search(current_word):
            if current_word[len(current_word) - 1] == ' " ':
                ends_with_quotes = True
            else:
                ends_with_quotes = False
            sentence += current_word + ' " ' if starts_with_quotes and not ends_with_quotes else current_word
            stop = True
        else:
            sentence += current_word + ' ' 
            current_word = random.choice(cache[current_word])     

    return sentence

for i in range(5):
    print("")
    print(generator())  
    print(" ")           