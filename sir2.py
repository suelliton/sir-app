import os
import requests
from bs4 import BeautifulSoup
from flask import jsonify
import re
import urllib





url = "http://127.0.0.1:4040/inspect/http"
html = urllib.urlopen(url).read()

urls = re.findall('https://.+?(?=["\'])', html)

for url in urls:
    print url
print urls[1]  
http = urls[1]  
requests.post("https://suelliton.pythonanywhere.com/url/",data={'url':http})