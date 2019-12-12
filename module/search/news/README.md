# naver_news_search

## Documents
https://developers.naver.com/docs/search/news/

## API 기본 정보
메서드 | 인증 | 요청 URL | 출력 포맷
-- | -- | -- | --
GET | - | https://openapi.naver.com/v1/search/news.xml | XML
GET | - | https://openapi.naver.com/v1/search/news.json | JSON

## 요청 변수 (request parameter)
요청 변수 | 타입 | 필수 여부 | 기본값 | 설명
-- | -- | -- | -- | --
query | string | Y | - | 검색을 원하는 문자열로서 UTF-8로 인코딩한다.
display | integer | N | 10(기본값), 100(최대) | 검색 결과 출력 건수 지정
start | integer | N | 1(기본값), 1000(최대) | 검색 시작 위치로 최대 1000까지 가능
sort | string | N | sim, date(기본값) | 정렬 옵션: sim (유사도순), date (날짜순)

## 출력 결과
필드 | 타입 | 설명
-- | -- | --
rss | - | 디버그를 쉽게 하고 RSS 리더기만으로 이용할 수 있게 하기 위해 만든 RSS 포맷의 컨테이너이며 그 외의 특별한 의미는 없다.
channel | - | 검색 결과를 포함하는 컨테이너이다. 이 안에 있는 title, link, description 등의 항목은 참고용으로 무시해도 무방하다.
lastBuildDate | datetime | 검색 결과를 생성한 시간이다.
total | integer | 검색 결과 문서의 총 개수를 의미한다.
start | integer | 검색 결과 문서 중, 문서의 시작점을 의미한다.
display | integer | 검색된 검색 결과의 개수이다.
item/items | - | XML 포멧에서는 item 태그로, JSON 포멧에서는 items 속성으로 표현된다. 개별 검색 결과이며 title, originallink, link, description, pubDate를 포함한다.
title | string | 개별 검색 결과이며, title, originallink, link, description, pubDate 를 포함한다.
originallink | string | 검색 결과 문서의 제공 언론사 하이퍼텍스트 link를 나타낸다.
link | string | 검색 결과 문서의 제공 네이버 하이퍼텍스트 link를 나타낸다.
description | string | 검색 결과 문서의 내용을 요약한 패시지 정보이다. 문서 전체의 내용은 link를 따라가면 읽을 수 있다. 패시지에서 검색어와 일치하는 부분은 태그로 감싸져 있다.
pubDate | datetime | 검색 결과 문서가 네이버에 제공된 시간이다.

## 에러 코드
HTTP 코드 | 에러 코드 | 에러 메시지 | 조치 방안
-- | -- | -- | --
400 | SE01 | Incorrect query request (잘못된 쿼리요청입니다.) | 검색 API 요청에 오류가 있습니다. 요청 URL, 필수 요청 변수가 정확한지 확인 바랍니다.
400 | SE02 | Invalid display value (부적절한 display 값입니다.) | display 요청 변수값이 허용 범위(1~100)인지 확인해 보세요.
400 | SE03 | Invalid start value (부적절한 start 값입니다.) | start 요청 변수값이 허용 범위(1~1000)인지 확인해 보세요.
400 | SE04 | Invalid sort value (부적절한 sort 값입니다.) | sort 요청 변수 값에 오타가 없는지 확인해 보세요.
400 | SE06 | Malformed encoding (잘못된 형식의 인코딩입니다.) | 검색어를 UTF-8로 인코딩하세요.
404 | SE05 | Invalid search api (존재하지 않는 검색 api 입니다.) | 검색 API 대상에 오타가 없는지 확인해 보세요.
500 | SE99 | System Error (시스템 에러) | 서버 내부 에러가 발생하였습니다. 포럼에 올려주시면 신속히 조치하겠습니다.

## response
### example - xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
    <channel><title>Naver Open API - news ::'주식'</title>
        <link>http://search.naver.com</link>
        <description>Naver Search Result</description>
        <lastBuildDate>Mon, 26 Sep 2016 11:01:35 +0900</lastBuildDate>
        <total>2566589</total>
        <start>1</start>
        <display>10</display>
        <item>
            <title>국내 <b>주식</b>형펀드서 사흘째 자금 순유출</title>
            <originallink>http://app.yonhapnews.co.kr/YNA/Basic/SNS/r.aspx?c=AKR20160926019000008&did=1195m</originallink>
            <link>http://openapi.naver.com/l?AAAC2NSwvCMBCEf832WJK06eOQg+kDLAqCXjyGJqUFk9i0Kv57t0VYdr+ZgZ35ZcJXQFPBIQFZbVBIKOtoDGYQ47o+ITkAa3Gc+SyxU28T4t5bNKyaHJ5glI7d6CBprdcGkvp0rYFldtLIi+mRl0lTFJRQFH4PyM7qz6TISZbmPFoFTfO04JyVnJE8smLADn3sBjlfmvMITFKF63Hbusuha+++xxc/Bc8nKskAAAA=</link>
            <description>국내 <b>주식</b>형 펀드에서 사흘째 자금이 빠져나갔다. 26일 금융투자협회에 따르면 지난 22일 상장지수펀드(ETF)를 제외한 국내 <b>주식</b>형 펀드에서 126억원이 순유출됐다. 472억원이 들어오고 598억원이 펀드... </description>
            <pubDate>Mon, 26 Sep 2016 07:50:00 +0900</pubDate>
        </item>
        ...
    </channel>
</rss>
```

### example - json
```json
{
  "lastBuildDate": "Thu, 12 Dec 2019 17:35:19 +0900",
  "total": 6040656,
  "start": 1,
  "display": 100,
  "items": [
    {
      "title": "데일리블록체인, 특별관계자 지분변동",
      "originallink": "http://news.kmib.co.kr/article/view.asp?arcid=0014025657&code=61141211&cp=nv",
      "link": "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=005&aid=0001267996",
      "description": "공시 전문으로 이동 * <b>주식</b>등의 대량보유상황보고서는 특수관계인을 포함한
      개인이나 법인이 상장회사 지분을 5%이상 보유하게 될 경우에 5일 이내 발표하는 지분공시다. 일명
      &quot;5%룰&quot;이라고도 불리며, <b>주식</b>을 추가로... ",
      "pubDate": "Thu, 12 Dec 2019 17:34:00 +0900"

    },
    {
      "title": "MSCI EM, 아람코 편입 공표..&quot;영향은 제한적&quot;",
      "originallink": "http://www.edaily.co.kr/news/newspath.asp?newsid=03804806622717864",
      "link": "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=018&aid=0004536134",
      "description": "12일 삼성증권에 따르면 아람코 <b>주식</b>은 11일 10%(사우디의 상, 하한가)의
      상한가를 기록, 종가 기준 전체 기업가치가 1억8770억달러로 집계됐다. 전체 <b>주식</b>수중 1.5%가
      공모됐는데 공모주 중 보호예수 물량이 존재해... ",
      "pubDate": "Thu, 12 Dec 2019 17:34:00 +0900"

    }
  ]
}
```
