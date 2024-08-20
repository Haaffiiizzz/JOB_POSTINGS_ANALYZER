from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import json

# url = 'https://www.amazon.ca/hz/wishlist/ls/1RSXQTAQQ6AQ2?ref_=wl_share'
url = 'https://www.amazon.ca/hz/wishlist/ls/N6BMVY7ONH?ref_=wl_share'

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options = chrome_options)
driver.get(url)

"""
code to ensure scrolling to end of wishlist
    
"""
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


soup = BeautifulSoup(driver.page_source, 'html.parser')

names = soup.find_all("h2", {"class": "a-size-base"})
prices = soup.find_all("span", {"class": "a-price"})


wishlist = {}

for name, price in zip(names, prices):

    name = name.text.strip()
    
    whole = price.find("span", {"class": "a-price-whole"})
    frac = price.find("span", {"class": "a-price-fraction"})
    
    price = f"{whole.text.strip()}{frac.text.strip()}"
    
    wishlist[name] = price

with open("wishlist.json", "w") as file:
    json.dump(wishlist, file, indent = 4)
    
