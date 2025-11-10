from multiprocessing import Process
import requests

def download (url):
    print(f"Downloading from {url}")
    res = requests.get(url)
    print(f"Downloaded from {url}")

if __name__ == '__main__':

    urls = [
        "https://httpbin.org/image/jpeg",
        "https://httpbin.org/image/png",
        "https://httpbin.org/image/svg",
    ]
    processes = [Process(target=download, args=(url,)) for url in urls]

    for process in processes:
        process.start()

    for process in processes:
        process.join()