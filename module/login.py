#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from urllib.error import HTTPError
from urllib.parse import urlencode
from pyvirtualdisplay import Display

from private.client import PrivateClient

client = PrivateClient()
def get_naver_token2():
    chromedriver_path = "./chromedriver"
    naver_id = client.naver_id
    naver_pw = client.naver_pw
    naver_cid = client.id
    naver_csec = client.secret
    naver_redirect = "https://blog.naver.com/darkq4"

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    #display = Display(visible=0, size=(800, 800))
    #display.start()

    driver = webdriver.Chrome(chromedriver_path)  # driver = webdriver.PhantomJS()
    state = "REWERWERTATE"
    req_url = 'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=%s&redirect_uri=%s&state=%s' % (naver_cid, naver_redirect, state)

    driver.implicitly_wait(3)
    driver.get(req_url, headers=headers)

    driver.execute_script(exid)
    driver.execute_script(expw)
    driver.execute_script("document.getElementById('frmNIDLogin').submit()")

    html = driver.page_source
    print(html)

    ##########################
    # XXX: 최초 1회만 반드시 필요하고 이후엔 불필요함
    driver.find_element_by_xpath('//*[@id="confirm_terms"]/a[2]').click()
    #driver.find_element_by_xpath("//button[@class='btn_unit_on']").click()
    #driver.execute_script( "document.querySelector('.btn_unit_on).click()")


    ##########################
    redirect_url = driver.current_url
    print(redirect_url)


    temp = re.split('code=', redirect_url)
    code = re.split('&state=', temp[1])[0]
    driver.quit()
    #display.stop()

    url = 'https://nid.naver.com/oauth2.0/token?'
    data = 'grant_type=authorization_code' + '&client_id=' + naver_cid + '&client_secret=' + naver_csec + '&redirect_uri=' + naver_redirect + '&code=' + code + '&state=' + state

    request = urllib.request.Request(url, data=data.encode("utf-8"))
    request.add_header('X-Naver-Client-Id', naver_cid)
    request.add_header('X-Naver-Client-Secret', naver_redirect)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    token = ''
    if rescode == 200:
        response_body = response.read()
        js = json.loads(response_body.decode('utf 8'))
        token = js['access_token']
    else:
        print("Error Code:", rescode)
        return None

    if len(token) == 0:
        return None
    print(token)
    return token

def get_naver_token():
  from selenium import webdriver
  from selenium.webdriver.common.action_chains import ActionChains
  from selenium.webdriver.common.keys import Keys
  import pyperclip
  import time

  chromedriver_path = "./chromedriver"
  naver_id = "darkq4"
  naver_pw = "Dmpo3535!@"
  naver_cid = client.id
  naver_csec = client.secret
  naver_redirect = "https://blog.naver.com/darkq4"

  #클립보드에 input을 복사한 뒤
  #해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
  def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

  driver = webdriver.Chrome('./chromedriver')
  state = "REWERWERTATE"
  driver.implicitly_wait(3)
  req_url = 'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=%s&redirect_uri=%s&state=%s' % (naver_cid, naver_redirect, state)
  print(req_url)
  driver.get(req_url)

  copy_input('//*[@id="id"]', naver_id)
  time.sleep(1)
  copy_input('//*[@id="pw"]', naver_pw)
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
  time.sleep(1)
  ##########################
  # XXX: 최초 1회만 반드시 필요하고 이후엔 불필요함
  #driver.find_element_by_xpath('//*[@id="confirm_terms"]/a[2]').click()
  driver.find_element_by_xpath("//button[@class='btn_unit_on']").click()
  ##########################

  redirect_url = driver.current_url
  print(redirect_url)

  temp = re.split('code=', redirect_url)
  code = re.split('&state=', temp[1])[0]
  driver.quit()

  url = 'https://nid.naver.com/oauth2.0/token?'
  data = 'grant_type=authorization_code' + '&client_id=' + naver_cid + '&client_secret=' + naver_csec + '&redirect_uri=' + naver_redirect + '&code=' + code + '&state=' + state

  request = urllib.request.Request(url, data=data.encode("utf-8"))
  request.add_header('X-Naver-Client-Id', naver_cid)
  request.add_header('X-Naver-Client-Secret', naver_redirect)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()
  token = ''
  if rescode == 200:
      response_body = response.read()
      js = json.loads(response_body.decode('utf 8'))
      token = js['access_token']
  else:
      print("Error Code:", rescode)
      return None

  if len(token) == 0:
      return None
  print(token)
  return token

get_naver_token()
