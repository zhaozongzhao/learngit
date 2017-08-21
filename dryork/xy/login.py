#主程序
from selenium import webdriver
import csv
import log
import Title
csv_reader = csv.reader(open('C:\\testing\\xy\\wpsc\\2.csv','r'))
url='http://xy.dryork.cn/xinyue_manage/admin/main'
log.log(url,csv_reader)


