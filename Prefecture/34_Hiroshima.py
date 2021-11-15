#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver 
import chromedriver_binary
import os 
import csv 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys as keys 

# In[6]:


browser = webdriver.Chrome()


# In[ ]:

browser.get('https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code=040000')


# In[ ]:
text = browser.find_element_by_id("short-table-container").text
print(text)
# %%
