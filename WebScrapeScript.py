import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = "https://lotto.bclc.com/winning-numbers.html"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

first_block = soup.find(class_="span11 winning-numbers")
soup = BeautifulSoup(first_block, 'html.parser')
second_block = soup.find(class_="list-items")