# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests as req
import time
import pdb

f = open('/home/xiaorui/Desktop/hongxian.txt', 'a+')

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'
}


def get_links(url):
    wb_info = req.get(url, headers=headers)
    soup = BeautifulSoup(wb_info.text, 'lxml')
    domain = url
    links = soup.select('body > div:nth-of-type(1) > table > tr:nth-of-type(4) > td > table:nth-of-type(2) > tbody > tr > td > a')
    for link in links:
        href = link.get('href')
        href = domain + '/' + href
        get_info(href)
        time.sleep(0.5)

def get_info(url):
    wb_info = req.get(url, headers=headers)
    wb_info.encoding = 'gbk'
    soup = BeautifulSoup(wb_info.text, 'lxml')
    title1 = soup.find_all('font')
    title = soup.select('body > div > table:nth-of-type(4)> tr:nth-of-type(1) > td > strong > font')
    if len(title) == 1:
        f.write(title[0].get_text().encode('utf8')+'\n')
    content = soup.select('body > div > table:nth-of-type(5)  > tr > td:nth-of-type(2) > p')
    if len(content) == 1:
        f.write(content[0].get_text().encode('utf8') + '\n\n\n')

if __name__=='__main__':
    urls = ['https://www.kanunu8.com/book3/7377',]
    for url in urls:
        get_links(url)

f.close()