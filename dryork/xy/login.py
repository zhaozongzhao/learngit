#主程序
import csv

from Basic_grammar import log

csv_reader = csv.reader(open('C:\\testing\\xy\\wpsc\\2.csv','r'))
url='http://xy.dryork.cn/xinyue_manage/admin/main'
log.log(url, csv_reader)


