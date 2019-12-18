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

  def news(self, p_query="주식", p_display="100", p_start="1", p_sort="sim", form="json"):
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

    params = {
        'query':p_query,
        'display':p_display,
        'start':p_start,
        'sort':p_sort
        }
    r = requests.get(url, headers=self.header, params=params)
    if r.status_code == 200:
      return json.loads(r.text)
    else:
      print("Error Code " + str(r.status_code))
      return None

  def trend(self):
    url = "https://openapi.naver.com/v1/datalab/search"
    headers = self.header
    headers["Content-Type"] = "application/json"

    data = '{"startDate":"2019-01-01","endDate":"2019-12-01","timeUnit":"month","keywordGroups":[{"groupName":"한글","keywords":["한글","korean"]},{"groupName":"영어","keywords":["영어","english"]}],"device":"pc","ages":["1","2"],"gender":"f"}'
    r = requests.post(url, headers=headers, data=data.encode("utf-8"))
    if r.status_code == 200:
      return json.loads(r.text)
    else:
      print("Error Code " + str(r.status_code))
      return None

#########################################################################################
# main
#########################################################################################

def main_news():
  api = NaverOpenApi()

  r = api.news()
  for item in r['items']:
    print(item['title'])

  print('---------------------------------------------------')

  r = api.news(p_start="100")
  for item in r['items']:
    print(item['title'])
    print(item['originallink'])
    print(item['link'])
    print(item['description'])
    print(item['pubDate'])

def main_trend():
  api = NaverOpenApi()
  r = api.trend()
  print(r)

if __name__ == '__main__':
  #main_news()
  main_trend()
