# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests as req
import time
import pdb

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
    url = 'http://www.kanunu8.com/files/writer/189.html'
    wb_info = req.get(url, headers=headers)
    wb_info.encoding = 'gbk'
    soup = BeautifulSoup(wb_info.text, 'lxml')
    domain = 'http://www.kanunu8.com/'
    links = soup.select('body > div:nth-of-type(1) > table > tr > td:nth-of-type(2) > table:nth-of-type(3) > tr > td > table > tbody > tr > td > a ')
    for link in links:
        href = link.get('href')
        href = domain + '/' + href
        name = '/home/xiaorui/Desktop/九把刀/' + link.get_text().encode('utf8') + '.txt'
        f = open(name, 'a+')
        get_links(href)
        f.close()
        time.sleep(1)

