# naver_news_search

## Documents
https://developers.naver.com/docs/datalab/search

## 파라미터 
파라미터 | 타입 | 필수 여부 | 설명
-- | -- | -- | --
startDate | string | Y | 조회 기간 시작 날짜(yyyy-mm-dd 형식). 2016년 1월 1일부터 조회할 수 있습니다.
endDate | string | Y | 조회 기간 종료 날짜(yyyy-mm-dd 형식)
timeUnit | string | Y | 구간 단위- date: 일간- week: 주간- month: 월간
keywordGroups | array(JSON) | Y | 주제어와 주제어에 해당하는 검색어 묶음 쌍의 배열. 최대 5개의 쌍을 배열로 설정할 수 있습니다.
keywordGroups.groupName | string | Y | 주제어. 검색어 묶음을 대표하는 이름입니다.
keywordGroups.keywords | array(string) | Y | 주제어에 해당하는 검색어. 최대 20개의 검색어를 배열로 설정할 수 있습니다.
device | string | N | 범위. 검색 환경에 따른 조건입니다.- 설정 안 함: 모든 환경- pc: PC에서 검색 추이- mo: 모바일에서 검색 추이
gender | string | N | 성별. 검색 사용자의 성별에 따른 조건입니다.- 설정 안 함: 모든 성별- m:남성- f: 여성
ages | array(string) | N | 연령. 검색 사용자의 연령에 따른 조건입니다.- 설정 안 함: 모든 연령- 1: 0∼12세- 2: 13∼18세- 3: 19∼24세- 4: 25∼29세- 5: 30∼34세- 6: 35∼39세- 7: 40∼44세- 8: 45∼49세- 9: 50∼54세- 10: 55∼59세- 11: 60세 이상

## 응답 
startDate | string | 조회 기간 시작 날짜(yyyy-mm-dd 형식).
-- | -- | --
endDate | string | 조회 기간 종료 날짜(yyyy-mm-dd 형식)
timeUnit | string | 구간 단위
results.title | string | 주제어
results.keywords | array | 주제어에 해당하는 검색어
results.data.period | string | 구간별 시작 날짜(yyyy-mm-dd 형식)
results.data.ratio | string | 구간별 검색량의 상대적 비율. 구간별 결과에서 가장 큰 값을 100으로 설정한 상댓값입니다.

## 오류 코드
오류 코드 | HTTP 상태 코드 | 오류 메세지 | 설명
-- | -- | -- | --
400 | 400 | 잘못된 요청 | API 요청 URL의 프로토콜, 파라미터 등에 오류가 있는지 확인합니다.
500 | 500 | 서버 내부 오류 | 서버 내부에 오류가 발생했습니다. "개발자 포럼"에 오류를 신고해 주십시오.
