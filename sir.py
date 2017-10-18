import os
import requests
from bs4 import BeautifulSoup

#abre tunel http e https
b = os.system("/home/suelliton/ngrok http 80")  
#fa requisicao a pagina localhost do ngrok para pegar a url
