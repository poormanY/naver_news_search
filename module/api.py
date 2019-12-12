import requests
import json

from private.client import PrivateClient

class NaverOpenApi:
  def __init__(self):
    client = PrivateClient()
    self.clientId = client.id
    self.clientSecret = client.secret
    self.header = {
      "X-Naver-Client-Id": self.clientId,
      "X-Naver-Client-Secret": self.clientSecret
    }

  def news(self, p_query="주식", p_display="100", p_start="1", p_sort="date", form="json"):
    ## parameters
    # p_query : string(udf-8)
    # p_display : 10~100
    # p_start : 1~1000
    # p_sort : "date" or "sim"
    ## response
    # title, originallink, link, description, pubDate
    url = "https://openapi.naver.com/v1/search/news"
    if form == "xml":
      url = "https://openapi.naver.com/v1/search/news.xml"
    parameters = "?query=" + p_query \
              + "&display=" + p_display \
              + "&start=" + p_start \
              + "&sort=" + p_sort
    r = requests.get(url + parameters, headers=self.header)
    return json.loads(r.text)

def main():
  api = NaverOpenApi()

  r = api.news()
  for item in r['items']:
    print(item['title'])

  print('---------------------------------------------------')

  r = api.news(p_start="100")
  for item in r['items']:
    print(item['title'])

if __name__ == '__main__':
  main()

