# -*- encoding: utf-8 -*-

import sys
sys.path.append("module")
import time

from module.api import NaverOpenApi
from module.crawl import WebCrawl
from module.blog import NaverBlog

def headline(kwds, category):
  # naver blog auto write
  blog = NaverBlog()

  # [AI 실시간 헤드라인 뉴스] 2019-12-16 06:32:22
  blogTitle = "[AI 실시간 헤드라인 뉴스] " + kwds['now']
  blogDescription = ""
  #category = "Politics"

  for kwd in kwds:
    if kwd == 'now':
      continue
    rankN = kwd
    item = kwds[kwd]
    headline = item['headline']
    lede = item['lede']
    link = item['link']
    blogDescription = blogDescription + "<h2>" + str(rankN) + ". " + headline + "</h2>" + lede + "<br>" + "<a href='" + link + "'>" + link + "</a>" + "<br>"
  blog.post(blogTitle, blogDescription, category)

def headline_politics():
  # headline crawling
  crawl = WebCrawl()
  kwds = crawl.headline_news_politics()
  category = "Politics"
  headline(kwds, category)

def headline_economy():
  # headline crawling
  crawl = WebCrawl()
  kwds = crawl.headline_news_economy()
  category = "Economy"
  headline(kwds, category)

def headline_society():
  # headline crawling
  crawl = WebCrawl()
  kwds = crawl.headline_news_society()
  category = "Society"
  headline(kwds, category)

def headline_life():
  # headline crawling
  crawl = WebCrawl()
  kwds = crawl.headline_news_life()
  category = "Life"
  headline(kwds, category)

def headline_world():
  # headline crawling
  crawl = WebCrawl()
  kwds = crawl.headline_news_world()
  category = "World"
  headline(kwds, category)

def headline_it():
  # headline crawling
  crawl = WebCrawl()
  kwds = crawl.headline_news_it()
  category = "IT"
  headline(kwds, category)

def main():
  headline_politics()
  headline_economy()
  headline_society()
  headline_life()
  headline_world()
  headline_it()

#########################################################################################
# main
#########################################################################################

if __name__ == '__main__':
  main()
