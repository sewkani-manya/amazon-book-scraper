# scraper.py

#import libraries
import requests
from bs4 import BeautifulSoup

#specify the url
bestseller_page ="https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_0"

#query the website and return the html of the variable
response=requests.get(bestseller_page)
#parse the HTML using beautiful soup and storing in a variable soup
soup=BeautifulSoup(response.content, "html.parser")
print(soup.encode("utf-8"))

# Take out the <div> of the name and get its value
book_name_div= soup.find("div", attrs={'class':'p13n-sc-truncate'})
