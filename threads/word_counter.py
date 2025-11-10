import threading
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

threads = []

for file in files:
    thread = threading.Thread(target=count_words, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


