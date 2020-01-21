import requests
import json
import urllib.request


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


  def papago(self, text, lang1="ko", lang2="en"):
    client_id = self.clientId # 개발자센터에서 발급받은 Client ID 값
    client_secret = self.clientSecret # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(text)
    data = "source=" + lang1 + "&target=" + lang2 + "&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        return json.loads(response_body)['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)
        return None

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

def main_papago():
  api = NaverOpenApi()
  lang1 = "en"
  lang2 = "ko"
  text = "I found a love for me"
  r = api.papago(text, lang1, lang2)
  print(r)

if __name__ == '__main__':
  #main_news()
  #main_trend()
  main_papago()
