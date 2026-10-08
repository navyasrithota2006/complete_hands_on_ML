'''
Rael world example : multithreading fori/o bound tasks
scenario : web scrapping

web scraping always involves making requests and waiting for the responses from servers.
multi threading can improve performance by allowing multiple web pages to be fetched concurrently

'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
  'https://python.langchain.com/v0.2/docs/introduction/',
  'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/',   
]

#the use of multithreading here is that i create 3 threads which concurrently do the web scraping thing fast in 3 webs givens,if the 
#responses are late other thread joins and extraqcts which improves the performances

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'fetched {len(soup.text)} characters from {url}')


threads = []
for url in urls:
    thread = threading.Thread(target = fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all web pages are fetched")