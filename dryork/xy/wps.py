# coding: utf-8
import csv
from itertools import islice
def reade():
 csv_reader = csv.reader((open('2.csv','r')))

def writer():
    list = ['1', '2','3','4']
    out = open('test.csv', 'w', newline='')
    csv_writer = csv.writer(out)
    csv_writer.writerow(list)
def jt(driver):
    n=1
    n='C:\\testing\\xy\\wpsc\\'+str(n)+'.jgp'
    print(n)
    driver.get_screenshot_as_file(n)
