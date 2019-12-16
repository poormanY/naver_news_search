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
  p_sort="date"
  form="json"

  # ranking keywords crawling top20
  crawl = WebCrawl()
  kwds = crawl.rank_kwds()

  # naver blog auto write
  blog = NaverBlog()

  # [AI 실시간 인기 키워드 뉴스] 2019-12-16 06:32:22
  blogTitle = "[AI 실시간 인기 키워드 뉴스] " + kwds['now']
  print(blogTitle)
  blogDescription = ""
  category = "NewsTrend"

  for kwd in kwds:
    if kwd == 'now':
      continue
    p_query = kwds[kwd]
    data = api.news(p_query=p_query, p_display=p_display, p_start=p_start, p_sort=p_sort, form=form)

    rankN = kwd
    title = data['items'][0]['title']
    link = data['items'][0]['link']
    description = data['items'][0]['description']
    pubDate = data['items'][0]['pubDate']
    for d in data['items']:
      print('+++++++++++++++++++++++++++')
      if 'naver.com' in d['link']:
        title = d['title']
        link = d['link']
        description = d['description'].encode('utf-8')
        pubDate = d['pubDate']
        print('-------------------------')
        break
    print(title)
    print(description)
    print(link)
    print(pubDate)

    print(str(rankN))
    print(str(link))
    print(str(pubDate))
    print('-------------------------')

    blogDescription = blogDescription + "<h4>" + str(rankN) + ". #" + str(title) + "</h4>" + "<ul>" + "<li>" + description +"</li>" + "<li>" + str(link) +"</li>" + "<li>" + str(pubDate) +"</li>" + "</ul>"
    time.sleep(10/60) # call api 10times per 1s

  #blog.post(blogTitle, blogDescription, category)

#########################################################################################
# main
#########################################################################################

if __name__ == '__main__':
  main()
