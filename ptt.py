# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests as req
import time
import pdb

f = open('/home/xiaorui/Desktop/ptt.txt', 'a+')

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'
}


def get_links(url):
    wb_info = req.get(url, headers=headers)
    soup = BeautifulSoup(wb_info.text, 'lxml')
    domain = 'https://www.ptt.cc'
    links = soup.select('#main-container > div.r-list-container.action-bar-margin.bbs-screen > div > div.title > a')
    for link in links:
        href = link.get('href')
        href = domain + href
        get_info(href)

def get_info(url):
    wb_info = req.get(url, headers=headers)
    soup = BeautifulSoup(wb_info.text, 'lxml')
    authors = soup.select('#main-content > div:nth-of-type(1) > span.article-meta-value')
    if len(authors) == 1:
        f.write('author:'+authors[0].get_text().encode('utf8')+'\n')
    titles = soup.select('#main-content > div:nth-of-type(3) > span.article-meta-value')
    if len(titles) == 1:
        f.write('title:'+titles[0].get_text().encode('utf8')+'\n')
    times = soup.select('#main-content > div:nth-of-type(4) > span.article-meta-value')
    if len(times) == 1:
        f.write('time:'+times[0].get_text().encode('utf8')+'\n')
    infos = soup.select('#main-content')
    if len(infos) == 1:
        f.write('info:'+infos[0].get_text().encode('utf8')+'\n\n')
    # for author,title, time, info in zip(authors, titles, times, infos):
    #     data = {
    #         'author': author.get_text(),
    #         'title': title.get_text(),
    #         'time': time.get_text(),
    #         'info': info.get_text(),
    #     }


if __name__=='__main__':
    urls = ['https://www.ptt.cc/bbs/Boy-Girl/index{}.html'.format(number) for number in [1,]]
    for url in urls:
        get_links(url)
        time.sleep(2)
f.close()