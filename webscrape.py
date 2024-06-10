
import requests as re
import json
from bs4 import BeautifulSoup
from requests_html import HTMLSession
s=HTMLSession()
 
url="https://www.jumia.com.ng/computer-accessories/"
response=re.get(url)
print(response.html.html)