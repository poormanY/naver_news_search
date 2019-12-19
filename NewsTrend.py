# -*- encoding: utf-8 -*-

import sys
sys.path.append("module")
import time

from module.api import NaverOpenApi
from module.crawl import WebCrawl
from module.blog import NaverBlog

def main():
  api = NaverOpenApi()
  p_query="주식"
  p_display="1"
  p_start="1"
  p_sort="sim"
  form="json"

  # ranking keywords crawling top20
  crawl = WebCrawl()
  kwds = crawl.rank_kwds()

  # naver blog auto write
  blog = NaverBlog()

  # [AI 실시간 인기 키워드 뉴스] 2019-12-16 06:32:22
  blogTitle = "[AI 실시간 인기 키워드 뉴스] " + kwds['now']
  blogDescription = ""
  category = "NewsTrend"

  for kwd in kwds:
    if kwd == 'now':
      continue
    p_query = kwds[kwd]
    data = api.news(p_query=p_query, p_display=p_display, p_start=p_start, p_sort=p_sort, form=form)
    time.sleep(10/60) # call api 10times per 1s

    rankN = kwd
    title = data['items'][0]['title']
    link = data['items'][0]['link']
    description = data['items'][0]['description']
    pubDate = data['items'][0]['pubDate']

    blogDescription = blogDescription + "<h2>" + str(rankN) + ". " + p_query + " - " + title + "</h2>" + description + "<br>" + "<a href='" + link + "'>" + link + "</a>" + "<br>"
  # Add Hash-Tags
  blogDescription = blogDescription + "<br>"
  for kwd in kwds:
    if kwd == 'now':
      continue
    tag = ''.join(kwds[kwd].split())
    blogDescription = blogDescription + "#" + tag + " "

  blog.post(blogTitle, blogDescription, category)

#########################################################################################
# main
#########################################################################################

if __name__ == '__main__':
  main()
