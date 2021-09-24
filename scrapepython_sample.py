#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver 
import chromedriver_binary
import os 
import csv 


# In[6]:


browser = webdriver.Chrome()


# In[ ]:


url = 'https://scraping.kikagaku.net/'
browser.get(url)


# In[ ]:


title_elem = browser.find_element_by_class_name('u_title')

print(title_elem.text)


# In[ ]:


title_elems = browser.find_elements_by_class_name('u_title')
len(title_elems)


# In[ ]:


title_elems[1].text


# In[ ]:


title_elems = browser.find_elements_by_class_name('u_title')

places = []
for title_elem in title_elems:
    elem = title_elem.find_element_by_tag_name('h2')
    places.append(elem.text)


# In[ ]:


places


# In[ ]:


from bs4 import BeautifulSoup as bs4


# In[ ]:


import requests 


# In[ ]:


url = 'https://scraping.kikagaku.net/'

res = requests.get(url)


# In[ ]:


soup = bs4(res.text, "html.parser")


# In[ ]:


print(soup.prettify())


# In[ ]:


kutikomi_contents = soup.select('.kutikomi')
print(kutikomi_contents)


# In[ ]:


kutikomi_contents = str(kutikomi_contents).split('<dd class="kutikomi">')[1:]
kutikomi_contents[0]


# In[ ]:


import re 

def preprocessing(kutikomi_content):
    kutikomi_content = re.sub('[a-zA-Z\<> /,]','',kutikomi_content)
    return kutikomi_content


# In[ ]:


kutikomi_content = preprocessing(kutikomi_contents[0])
kutikomi_content


# In[ ]:


kutikomi_list = []
for j in kutikomi_contents:
    kutikomi_list.append(preprocessing(j))


# In[ ]:


kutikomi_list


# In[ ]:


import pandas as pd 
df = pd.DataFrame({
    '口コミ':kutikomi_list,
})


# In[ ]:


df 


# In[ ]:


url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2021&month=09&day=01&view=p1'
res = requests.get(url)


# In[ ]:


soup = bs4(res.text, "html.parser")


# In[ ]:


print(soup.prettify())


# In[ ]:


#bosaitop-bosai_forecast_table_div > div:nth-child(1) > div > div > div.contents-wide-table-scroll > table > tr:nth-child(4) > th


# In[ ]:


#bosaitop-bosai_forecast_table_div > div:nth-child(1) > div > div > div.contents-wide-table-scroll > table > tr:nth-child(4) > td:nth-child(3)


# In[ ]:


#\34 7590 > div:nth-child(1) > div > div:nth-child(3) > span:nth-child(2) > span


# In[ ]:


elems = soup.select('bosaitop-bosai_forecast_table_div > div:nth-of-type(1) > div > div > div.contents-wide-table-scroll > table > tr:nth-of-type(4) > td:nth-of-type(2)') 


# In[ ]:


elems


# In[ ]:


ele = soup.find_all('td', class_='data_0_0')


# In[ ]:


ele


# In[ ]:


#tablefix1 > tbody > tr:nth-child(5) > td:nth-child(1)
ele[]


# In[ ]:


ele[1].string


# In[ ]:


trs = soup.find("table", {"class" : "data2_s"})


# In[ ]:


data_list =[]
data_list_per_day = []


# In[ ]:


tds = trs.findAll('td')


# In[ ]:


trs.findAll('tr')[6].findAll('td')


# In[ ]:


def str2float(weather_data):
    try:
        return float(weather_data)
    except:
        return 0


# In[ ]:



for tr in trs.find_all('tr')[4:]:
    tds = tr.find_all('td')
    
    if tds[1].string == None:
        break;
    
    data_list.append(tds[0].string)
    data_list.append(str2float(tds[1].string)) #現地気圧平均（hPa）
    data_list.append(str2float(tds[2].string)) #海面気圧平均（hPa）
    if tds[3].string=='--':
        data_list.append(tds[3].string)  #合計降水量（㎜）
        #data_list.append(None)
    else:
        data_list.append(str2float(tds[3].string))
        
    if tds[4].string=='--':
        data_list.append(tds[4].string)#一時間当たり最大降水量（㎜）
        #data_list.append(None)
    else:
        data_list.append(str2float(tds[4].string))
        
    if tds[5].string=='--':
        data_list.append(tds[5].string)  #10分間当たり最大降水量（㎜）
        #data_list.append(None)
    else:
        data_list.append(str2float(tds[5].string))
    data_list.append(str2float(tds[6].string)) #平均気温（℃）
    data_list.append(str2float(tds[7].string)) #最高気温（℃）
    data_list.append(str2float(tds[8].string)) #最低気温（℃）
    data_list.append(str2float(tds[9].string)) #平均湿度（％）
    data_list.append(str2float(tds[10].string)) #最小湿度（％）
    data_list.append(str2float(tds[11].string)) #平均風速（m／s）
    data_list.append(str2float(tds[12].string)) #最大風速（m／s）
    data_list.append(None) #最大風速の風向（m／s）
    data_list.append(str2float(tds[14].string)) #最大瞬間風速（m／s）
    data_list.append(None) #最大瞬間風速の風向（m／s）
    data_list.append(str2float(tds[16].string)) #降雪量合計（㎝）
    data_list.append(str2float(tds[17].string)) #最深降雪（㎝）
    data_list.append(None) #天気概要　昼
    data_list.append(None) #天気概要　夜
    data_list_per_day.append(data_list)
    data_list = []
"""    
    if tds[18].string=='--':
        data_list.append(tds[18].string) #天気概要　昼
        #data_list.append(None)
    else:
        data_list.append(str2float(tds[18].string))
    if tds[19].string=='--':
        data_list.append(tds[19].string) #天気概要　夜
        #data_list.append(None)
    else:
        data_list.append(str2float(tds[19].string))
"""
    
    


# In[ ]:


data_list_per_day[0]


# In[ ]:


tds


# In[ ]:


list_sample = []
list_sample.append(2)


# In[ ]:


list_sample


# In[ ]:


list_sample.append(3)
list_sample


# In[ ]:


list_sample.append(None)


# In[ ]:


list_sample


# In[ ]:


string('2')
str2float


# In[1]:


import os 
import datetime
import csv 
import requests
from bs4 import BeautifulSoup as bs4
def str2float(weather_data):
    try:
        return float(weather_data)
    except:
        return 0

def scraping():

    url='http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2021&month=09&day=01&view=p1'
    res=requests.get(url)
    soup=bs4(res.text, "html.parser")
    trs = soup.find("table", {"class" : "data2_s"})

    data_list = []
    data_list_per_day=[]

    for tr in trs.findAll('tr')[4:]:
        tds = tr.findAll('td')

        data_list.append(tds[0].string)
        data_list.append(str2float(tds[1].string)) #現地気圧平均（hPa）
        data_list.append(str2float(tds[2].string)) #海面気圧平均（hPa）
        if tds[3].string=='--':
            data_list.append(tds[3].string)  #合計降水量（㎜）
            #data_list.append(None)
        else:
            data_list.append(str2float(tds[3].string))
        
        if tds[4].string=='--':
            data_list.append(tds[4].string)#一時間当たり最大降水量（㎜）
            #data_list.append(None)
        else:
            data_list.append(str2float(tds[4].string))
        
        if tds[5].string=='--':
            data_list.append(tds[5].string)  #10分間当たり最大降水量（㎜）
            #data_list.append(None)
        else:
            data_list.append(str2float(tds[5].string))
        data_list.append(str2float(tds[6].string)) #平均気温（℃）
        data_list.append(str2float(tds[7].string)) #最高気温（℃）
        data_list.append(str2float(tds[8].string)) #最低気温（℃）
        data_list.append(str2float(tds[9].string)) #平均湿度（％）
        data_list.append(str2float(tds[10].string)) #最小湿度（％）
        data_list.append(str2float(tds[11].string)) #平均風速（m／s）
        data_list.append(str2float(tds[12].string)) #最大風速（m／s）
        data_list.append(None) #最大風速の風向（m／s）
        data_list.append(str2float(tds[14].string)) #最大瞬間風速（m／s）
        data_list.append(None) #最大瞬間風速の風向（m／s）
        data_list.append(str2float(tds[16].string)) #降雪量合計（㎝）
        data_list.append(str2float(tds[17].string)) #最深降雪（㎝）
        data_list.append(None) #天気概要　昼
        data_list.append(None) #天気概要　夜
        data_list_per_day.append(data_list)
        data_list = []
    
    
    return data_list_per_day


# In[3]:


scraping()[0][6]


# Seleniumを使ってみる

# In[2]:


from selenium import webdriver 
from selenium.webdriver.common.keys import Keys as keys 


# In[9]:



browser = webdriver.Chrome()


# In[10]:


browser.get('https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code=040000')


# In[14]:


text = browser.find_element_by_id("short-table-container").text


# In[17]:


text


# In[24]:


s_blank = 'one two     three\nfour\tfive\usix'


# In[19]:


print(s_blank)


# In[20]:


spl = s_blank.split()
print(s_blank.split())


# In[22]:


spl[0]


# In[23]:


s_blank[0]


# In[25]:


print(text.split())


# In[27]:


browser.get("https://www.jma.go.jp/bosai/#pattern=forecast&area_type=class20s&area_code=0410001")


# In[28]:


text2 = browser.find_element_by_id("bosaitop-forecast_table_window").text


# In[29]:


text2


# In[30]:


print(text2.split())


# In[ ]:




