import string
from collections import Counter

file = "messy_text.txt"
output_file = "word_count.txt"

# Create a translation table to remove punctuation
translator = str.maketrans("", "", string.punctuation)

word_counter = Counter()

with open(file, "r", encoding="UTF-8") as f:
    for line in f:
        line = line.lower()
        line = line.translate(translator)
        words = line.strip().split()
        word_counter.update(words)

sorted_words = word_counter.most_common()

with open(output_file, "w", encoding="utf-8") as f:
    for word, count in sorted_words:
        f.write(f"{word}\t{count}\n")