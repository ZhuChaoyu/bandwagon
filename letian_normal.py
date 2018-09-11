# coding=utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8') 
import re
import time
from selenium import webdriver
##import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
import traceback

import string

sys.path.append("..")

from cysendmail import pro_send

def getContent(prdNo_map):

    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

    phantomjs_path = '/usr/local/src/phantomjs/bin/phantomjs'
    browser = webdriver.PhantomJS(phantomjs_path)
    browser.maximize_window()

####################

####################


    for prdNo in prdNo_map:
        pname = prdNo_map[prdNo]
        print '【乐天】' + pname
        url = 'http://chn.lottedfs.com/kr/product/productDetail?prdNo=' + prdNo 
        ##10002331513'
        print url

        browser.get(url)

        isTry_cart = True
        try:
            print browser.find_element_by_xpath('//*[@id="prdDetailTopArea"]/div[2]/div[2]/div[4]/span').text
        except:
            traceback.print_exc()
        else:
            isTry_cart = False
    
        if isTry_cart:
            print 'try to check cart'
            try:
                browser.find_element_by_xpath('//*[@id="prdCartBtn"]').click()
                print 'a'
                browser.find_element_by_xpath('//*[@id="contentArea"]/ul/li[4]/a').click()
                print 'go to cart'
    
                productname = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div[2]').text
                price = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/div[2]').text
            except:
                traceback.print_exc()
            else:
                print 'sucess crawl'
                print productname
                print price
                sendmail_res = pro_send(url,prdNo,pname)
                print sendmail_res


####################

    print 'aaaa'

    time.sleep(1)
    browser.quit()


if __name__ == '__main__':

    prdNo_map = { '10002290548':'test mail'
                 ,'10002331513':'SK2小灯泡'
                 ,'10003136185':'SK-II 体验装'
                 ,'10002223101':'施华洛世奇 小黑天鹅金'
                 }
    getContent(prdNo_map)



