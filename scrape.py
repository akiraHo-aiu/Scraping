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
print(scraping())
