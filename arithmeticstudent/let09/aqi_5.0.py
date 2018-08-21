'''
2.0json格式处理
3.0csv文件操作
4.0判断文件格式
5.0爬取天气情况
'''

import requests

def url_text_get(url):
    '''
   返回url的文本
    '''
    txt = requests.get(url,timeout = 30 )
   # print(txt.status_code)
    return txt.text




def main():
    '''
    主函数
    '''
    city = input('请输入城市的拼音：')
    url = 'http://pm25.in/'+ city

    url_str_text = url_text_get(url)
    #print(url_str_text)

    div_str = '''<div class="span12 data1">
        <div class="span1">
          <div class="value">
            '''
    index = url_str_text.find(div_str)
    begin_index = index + len(div_str)
    end_index = begin_index+2
    aqi_val = url_str_text[begin_index:end_index]
    print('空气质量为aqi :{}'.format(aqi_val))



if __name__ == '__main__':
    main()