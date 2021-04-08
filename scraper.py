# scraper.py

#import libraries
import requests
from bs4 import BeautifulSoup

#specify the url
bestseller_page ="https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_0"

#query the website and return the html of the variable
response=requests.get(bestseller_page)
