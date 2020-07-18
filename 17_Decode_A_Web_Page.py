import requests
import bs4

url = 'https://www.nytimes.com'
r = requests.get(url)

r_html = r.text

soup = bs4.BeautifulSoup(r_html, features = 'lxml')

# ???????


