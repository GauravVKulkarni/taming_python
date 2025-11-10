from concurrent.futures import ThreadPoolExecutor
import string

files = ["threads/sample_txt/1.txt", "threads/sample_txt/2.txt", "threads/sample_txt/3.txt", "threads/sample_txt/4.txt"]

translator = str.maketrans("", "", string.punctuation)

def count_words(file_path):

    count = 0

    with open(file_path, "r") as f:

        print(f"Processing {file_path}...")

        for line in f:
            line = line.lower()
            line = line.translate(translator)
            words = line.strip().split()
            count += len(words)

    print(f"Total words in {file_path}: {count}")
    return count

with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(count_words, files)

print(list(result))
print("All files have been processed.")