#what will happen when u download multiple images (its an i/o bound operation)

import threading
import requests
import time


def download(url):
        print(f"Starting to download from {url}")
        resp = requests.get(url)
        print(f"Finished downloading the {url}, size : {len(resp.content)} bytes.")

urls = [
        "https://httpbin.org/image/png",
        "https://httpbin.org/image/svg",
        "https://httpbin.org/image/jpeg"
]

start = time.time()
threads = []

# start all thread and append in a list 
for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t) #appends in the threads 

# join threads together
for t in threads:
      t.join()

end = time.time()

print(f"All files downloaded in {end-start:.2f} seconds.")

# Output
# Starting to download from https://httpbin.org/image/png
# Starting to download from https://httpbin.org/image/svg
# Starting to download from https://httpbin.org/image/jpeg
# Finished downloading the https://httpbin.org/image/png, size : 8090 bytes.
# Finished downloading the https://httpbin.org/image/jpeg, size : 35588 bytes.
# Finished downloading the https://httpbin.org/image/svg, size : 8984 bytes.
# All files downloaded in 3.31 seconds.