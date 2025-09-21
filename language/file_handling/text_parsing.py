import string
from collections import Counter

file = "messy_text.txt"
output_file = "cleaned_text.txt"

# Create a translation table to remove punctuation
translator = str.maketrans("", "", string.punctuation)

# Initialize word frequency counter
word_counter = Counter()

#file input
with open(file, "r", encoding="UTF-8") as f:
    for line in f:
        line = line.lower()
        line = line.translate(translator)
        words = line.strip().split()
        word_counter.update(words)

sorted_words = word_counter.most_common()

# Write cleaned word counts to a file ---
with open(output_file, "w", encoding="utf-8") as f:
    for word, count in sorted_words:
        f.write(f"{word}\t{count}\n")