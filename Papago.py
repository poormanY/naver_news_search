# -*- encoding: utf-8 -*-

import sys
sys.path.append("module")
import time

from module.api import NaverOpenApi
from module.blog import NaverBlog

def main():
  # naver blog auto write
  blog = NaverBlog()

  # [AI 팝송 자동번역]
  popTitle = "Ed Sheeran - Perfect"
  blogTitle = "[AI 팝송 자동번역] " + popTitle
  blogDescription = ""
  category = "PopsongEnc"

  api = NaverOpenApi()
  lang1 = "en"
  lang2 = "ko"
  texts = [
    "I found a love for me",
    "Darling just dive right in",
    "And follow my lead",
    "Well I found a girl beautiful and sweet",
    "I never knew you were the someone waiting for me",
    "'Cause we were just kids when we fell in love",
    "Not knowing what it was",
    "I will not give you up this time",
    "But darling, just kiss me slow, your heart is all I own",
    "And in your eyes you're holding mine",
    "Baby, I'm dancing in the dark with you between my arms",
    "Barefoot on the grass, listening to our favorite song",
    "When you said you looked a mess, I whispered underneath my breath",
    "But you heard it, darling, you look perfect tonight",
    "Well I found a woman, stronger than anyone I know",
    "She shares my dreams, I hope that someday I'll share her home",
    "I found a love, to carry more than just my secrets",
    "To carry love, to carry children of our own",
    "We are still kids, but we're so in love",
    "Fighting against all odds",
    "I know we'll be alright this time",
    "Darling, just hold my hand",
    "Be my girl, I'll be your man",
    "I see my future in your eyes",
    "Baby, I'm dancing in the dark, with you between my arms",
    "Barefoot on the grass, listening to our favorite song",
    "When I saw you in that dress, looking so beautiful",
    "I don't deserve this, darling, you look perfect tonight",
    "Baby, I'm dancing in the dark, with you between my arms",
    "Barefoot on the grass, listening to our favorite song",
    "I have faith in what I see",
    "Now I know I have met an angel in person",
    "And she looks perfect",
    "I don't deserve this",
    "You look perfect tonight"
  ]

  blogDescription = "<h3>" + blogDescription + popTitle + "</h3>"
  for text in texts:
    textEnc = api.papago(text, lang1, lang2)
    blogDescription = blogDescription + text + "<br>"
    blogDescription = blogDescription + textEnc + "<br>"
  # add hash tag
  # to do

  blog.post(blogTitle, blogDescription, category)

#########################################################################################
# main
#########################################################################################

if __name__ == '__main__':
  main()
