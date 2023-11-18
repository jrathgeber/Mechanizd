import threading
import requests

def download_url(url):
    response = requests.get(url)
    print(f"Downloaded {url}")

urls = ["https://www.example.com", "https://www.google.com", "https://www.github.com"]

# Create and start a thread for each URL
threads = []
for url in urls:
    thread = threading.Thread(target=download_url, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
# Rather than downloading the urls sequentially, the requests are sent similutatncy
print("All downloads complete.")