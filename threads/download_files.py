import threading
import time

def download_file(file_name, file_url, eta):
    print(f"Starting download {file_name} from {file_url}")
    time.sleep(eta)  # Simulate download time
    print(f"Finished downloading {file_name} from {file_url}")

file_repository = {
    "file1": ("http://example.com/file1", 3),
    "file2": ("http://example.com/file2", 5),
    "file3": ("http://example.com/file3", 0),
    "file4": ("http://example.com/file4", 4),
}

threads = []

for file_name, (url, eta) in file_repository.items():
    threads.append(threading.Thread(target = download_file, args=(file_name, url, eta)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()