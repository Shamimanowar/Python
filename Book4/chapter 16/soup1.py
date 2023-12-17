from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"

response = requests.get(url)
text = response.text
# print(response.status_code)
# print(text)


soup : object = BeautifulSoup(text, 'html.parser')
print(soup.title)

links = soup.find_all("a")
book_links = [name.get('href') for name in links]
# print(links[:10])


for book in book_links[1:]:
    print(url + book)
