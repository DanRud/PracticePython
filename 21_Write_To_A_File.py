import requests
import bs4

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
name_file = input('Specify the name of the output file that wil be saved .txt format: ')

r = requests.get(url)

soup = bs4.BeautifulSoup(r.text, 'html.parser')

with open(name_file, 'w') as open_file:
    for text in soup.find_all('p'):
        open_file.write(text.getText().strip())
