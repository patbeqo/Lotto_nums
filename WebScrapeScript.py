import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Location of chromedriver.exe
chromedriver = '/mnt/c/Program Files/chromedriver.exe'

# Below fixes issues with the dynamic webpage replacing HTML content
options = webdriver.ChromeOptions()
options.add_argument('headless')

browser= webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

# Website to scrape from
url = "https://lotto.bclc.com/winning-numbers.html"

# Grabs HTML from Website in order to parse
browser.get(url)
content = browser.page_source
soup = BeautifulSoup(content, 'html.parser')

# Parsing in order to find the lotto numbers
lotto_nums = soup.find(class_="span29 lotto-649-numbers").find("li")

print (lotto_nums)

