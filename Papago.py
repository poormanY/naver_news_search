# -*- encoding: utf-8 -*-

import sys
sys.path.append("module")
import time

from module.api import NaverOpenApi
from module.blog import NaverBlog

def read_pop_file(fname="popsong.txt"):
  data = dict()

  f = open(fname, 'r')
  data['singer_en'] = f.readline().strip()
  data['singer_kor'] = f.readline().strip()
  data['title_en'] = f.readline().strip()
  data['title_kor'] = f.readline().strip()
  data['youtube'] = f.readline().strip()
  data['lyrics'] = [line.rstrip() for line in f]
  f.close()

  return data

def main():
  data = read_pop_file()
  # naver blog auto write
  blog = NaverBlog()

  # [AI 팝송 자동번역]
  popTitle = data["singer_en"] + " - " + data["title_en"]
  blogTitle = data["singer_kor"] + " - " + data["title_kor"] + " 가사 번역 해석 발음"
  blogDescription = ""
  category = "PopsongEnc"

  api = NaverOpenApi()
  lang1 = "en"
  lang2 = "ko"
  texts = data["lyrics"]

  blogDescription = blogDescription + data['youtube'] + "<br>"
  blogDescription = "<h3>" + blogDescription + popTitle + "</h3>"
  for text in texts:
    textEnc = api.papago(text, lang1, lang2)
    blogDescription = blogDescription + text + "<br>"
    blogDescription = blogDescription + textEnc + "<br>"
  # add hash tag
  tags = []
  tags.append(''.join(data['singer_en'].split()))
  tags.append(''.join(data['singer_kor'].split()))
  tags.append(''.join(data['title_en'].split()))
  tags.append(''.join(data['title_kor'].split()))
  tags.append("가사")
  tags.append("번역")
  tags.append("해석")
  tags.append("발음")
  tags.append("자동번역")
  for tag in tags:
    blogDescription = blogDescription + "#" + tag + " "

  blog.post(blogTitle, blogDescription, category)

#########################################################################################
# main
#########################################################################################

if __name__ == '__main__':
  main()
