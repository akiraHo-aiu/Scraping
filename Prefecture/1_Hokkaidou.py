#!/usr/bin/env python
# coding: utf-8

# In[5]:

#ライブラリをロード
from selenium import webdriver 
import chromedriver_binary
import os 
import csv 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys as keys 

# In[6]:

#使用するブラウザーを指定　-- 都合が悪ければChrome以外のドライバーを用いればそれに応じたブラウザーも使用可能

browser = webdriver.Chrome()


# In[ ]:

#使用したいデータ、表があるURLを読み込む
browser.get('https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code=040000')


# In[ ]:
#find_element_by_id の””の中身を帰ることで取り出すデータを指定することができる。
text = browser.find_element_by_id("short-table-container").text
print(text)
# %%
