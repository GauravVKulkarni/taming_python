import threading
import time

stop_event = threading.Event()

def download_file(file_url, eta):
    time.sleep(eta)
    print(f"Downloaded: {file_url} in {eta} seconds")

def downloader_simulator():
    while not stop_event.is_set():
        if not threading.active_count() > 1:
            break
        print("Downloading....")
        time.sleep(1)

main_thread = threading.Thread(target=downloader_simulator)

main_thread.start()

file_urls = [
    ("http://example.com/file1", 9),
    ("http://example.com/file2", 5),
    ("http://example.com/file3", 7),
    ("http://example.com/file4", 12),
]

threads = []

for url, eta in file_urls:
    download_thread = threading.Thread(target=download_file, args=(url, eta))
    download_thread.start()
    threads.append(download_thread)

for thread in threads:
    thread.join()

stop_event.set()
main_thread.join()

print("All downloads completed.")