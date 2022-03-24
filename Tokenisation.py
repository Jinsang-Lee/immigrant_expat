import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse

pagenum=190
count=1
searchlist = []


p= input('how many pages to crawl?')
lastpage= int(p) * 10 -9

while pagenum < lastpage+1 :
    url = f'https://www.google.com/search?q=expat&tbs=cdr:1,cd_min:1/1/2015,cd_max:12/31/2021&start={pagenum}&sa=N&filter=0&2&biw=1920&bih=969&dpr=1'
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    r = soup.select('.jtfYYd')

    for i in r:
        temp = []
        temp.append(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
        temp.append(i.select_one('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf').text)
        searchlist.append(temp)


    driver.close()

    k=open('expat2.csv', 'w', encoding='utf-8', newline='')
    csvWriter = csv.writer(k)
    for i in searchlist:
        csvWriter.writerow((i))
    k.close()
    pagenum += 10
    count += 1

print('completed')