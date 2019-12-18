import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display

class WebCrawl:
  def dynamic_crawl(self):
    # output : { now:time, 1:kwd1, ..., 20:kwd20}
    output = {}
    now = str(datetime.now())
    output["now"] = now

    display = Display(visible=0, size=(800, 800))
    display.start()

    url = "https://www.naver.com"
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(1) # seconds
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    kwds = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
    for idx, kwd in enumerate(kwds, 1):
      output[idx] = kwd.text

    driver.quit()
    display.stop()
    return output

  def rank_kwds(self):
    # output : { now:time, 1:kwd1, ..., 20:kwd20}
    output = {}
    now = str(datetime.now())
    output["now"] = now

    url = "https://www.naver.com"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    kwds = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
    for idx, kwd in enumerate(kwds, 1):
      output[idx] = kwd.text
    return output

  def stock_rise(self, num=10):
    # output : { now:time, 1:kwd1, ... }
    output = {}
    now = str(datetime.now())
    output["now"] = now

    url = "https://finance.naver.com/sise/sise_rise.nhn"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    kwds = soup.find('table', {'class':'type_2'}).find_all('a', {'class':'tltle'})
    for idx, kwd in enumerate(kwds, 1):
      if idx > num:
          break
      output[idx] = kwd.text
    return output

  def stock_fall(self, num=10):
    # output : { now:time, 1:kwd1, ... }
    output = {}
    now = str(datetime.now())
    output["now"] = now

    url = "https://finance.naver.com/sise/sise_fall.nhn"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    kwds = soup.find('table', {'class':'type_2'}).find_all('a', {'class':'tltle'})
    for idx, kwd in enumerate(kwds, 1):
      if idx > num:
          break
      output[idx] = kwd.text
    return output

#########################################################################################
# main
#########################################################################################

def main_kwds():
  crawl = WebCrawl()
  kwds = crawl.rank_kwds()
  print(kwds)

def main_dynamic():
  crawl = WebCrawl()
  kwds = crawl.dynamic_crawl()
  print(kwds)

def main_stock_rise():
  crawl = WebCrawl()
  kwds = crawl.stock_rise()
  print(kwds)

def main_stock_fall():
  crawl = WebCrawl()
  kwds = crawl.stock_fall()
  print(kwds)

if __name__ == '__main__':
  #main_kwds()
  #main_dynamic()
  #main_stock_rise()
  main_stock_fall()
