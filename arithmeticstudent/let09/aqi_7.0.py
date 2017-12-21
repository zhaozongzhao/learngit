'''
2.0json格式处理
3.0csv文件操作
4.0判断文件格式
5.0爬取天气情况
6.0 使用beautifulsoup 解析网页
7.0获取城市列表
'''

import requests
from bs4 import BeautifulSoup

def get_aqi_list(city):
    '''
   返回url的文本
    '''
    url = 'http://pm25.in/' + city
    txt = requests.get(url,timeout = 30 )
    bs = BeautifulSoup(txt.text,'lxml')
    #soup = BeautifulSoup(r.text, 'lxml')
   #div_list = bs.find_all('div',{'class_' : 'span1'})
    div_list = bs.find_all('div', {'class': 'span1'})
    city_aqi = []
    for i in range(8):
        list_caption = div_list[i]
        div_value = list_caption.find('div',{'class':'value'}).text.strip()
        div_caption = list_caption.find('div',{'class':'caption'}).text.strip()

        city_aqi.append((div_caption,div_value))
    return city_aqi




def get_city_all():
    '''获取城市信息'''
    url = 'http://pm25.in'
    city_list = []
    r = requests.get(url,timeout = 30 )
    bs = BeautifulSoup(r.text,'lxml')
    div_list = bs.find_all('div',{'class':'bottom'})[1]
    a_list = div_list.find_all('a')

    # city_div = soup.find_all('div', {'class': 'bottom'})[1]
    # city_link_list = city_div.find_all('a')

    for i in a_list:
        name = i.text
        url = i['href'][1:]
        city_list.append((name,url))
    return city_list

def main():
    '''
    主函数
    '''
    city = get_city_all()
    for i in city:
        name = i[0]
        city = i[1]
        print(name)
        aqi_list = get_aqi_list(city)
        print(name,aqi_list)

    print(aqi_list)



if __name__ == '__main__':
    main()