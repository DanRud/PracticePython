import requests
import bs4

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url)

soup = bs4.BeautifulSoup(r.text, 'html.parser')

for text in soup.find_all('p'):
    print(text.getText())

