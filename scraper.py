# scraper.py
# TODO:
# - Update readme with all details about how you went through this project

#import libraries
import requests
from bs4 import BeautifulSoup

#specify the url
bestseller_url = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_0"

#query the website and return the html of the variable
response = requests.get(bestseller_url)

#parse the HTML using beautiful soup and storing in a variable soup
page = BeautifulSoup(response.content, "html.parser")

# Take out the <div> of the name and get its value
book_name_divs = page.find_all("div", attrs={'class':'p13n-sc-truncate'})

print("Amazon Bestseller's List:")
for b in book_name_divs:
    print(b.get_text())
