import requests as req
from bs4 import BeautifulSoup
import pdb


# Computational Chemistry Comparison and Benchmark DataBase
url = 'https://cccbdb.nist.gov/getform.asp'

# My request headers for website
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'
}
# Input structure information
params = {
    'formula':'C5H8O',
}


# Submit the form and find the structure
res = req.post(url, params, headers=headers)

print(res.url)
pdb.set_trace()

# print the html file
try:
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())
except req.ConnectionError:
    print('connection failure.')


