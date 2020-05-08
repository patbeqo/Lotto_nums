from selenium import webdriver
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook

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
lotto_nums = soup.find(class_="span29 lotto-649-numbers").find("li").get_text()

lotto_nums = list(lotto_nums.split(' ')) # converts string to list
lotto_nums.pop() # remove the last element which was ' '

# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

# writing to excel sheet
sheet1.write(1, 0, lotto_nums[0]) 
sheet1.write(1, 1, lotto_nums[1]) 
sheet1.write(1, 2, lotto_nums[2]) 
sheet1.write(1, 3, lotto_nums[3]) 
sheet1.write(1, 4, lotto_nums[4]) 
sheet1.write(1, 5, lotto_nums[5]) 

wb.save('excel_test.xls') 

exit()