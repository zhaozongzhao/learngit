'''
2.0json格式处理
3.0csv文件操作
4.0判断文件格式
5.0爬取天气情况
6.0 使用beautifulsoup 解析网页
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




def main():
    '''
    主函数
    '''
    city = input('请输入城市的拼音：')
    aqi_list = get_aqi_list(city)

    print(aqi_list)



if __name__ == '__main__':
    main()