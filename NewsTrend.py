import sys
sys.path.append("module")
import time

from module.api import NaverOpenApi
from module.crawl import WebCrawl

def main():
  api = NaverOpenApi()
  p_query="주식"
  p_display="1"
  p_start="1"
  p_sort="date"
  form="json"

  data = api.news(p_query=p_query, p_display=p_display, p_start=p_start, p_sort=p_sort, form=form)

  crawl = WebCrawl()
  kwds = crawl.rank_kwds()

  for kwd in kwds:
    p_query = kwds[kwd]
    data = api.news(p_query=p_query, p_display=p_display, p_start=p_start, p_sort=p_sort, form=form)
    print(kwd, kwds[kwd])
    print (data)
    time.sleep(10/60) # call api 10times per 1s

#########################################################################################
# main
#########################################################################################

if __name__ == '__main__':
  main()
