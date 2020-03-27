from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,traceback,test,time

browser = webdriver.Chrome()
#開啟google首頁
browser.get('https://www.instagram.com/?hl=zh-tw')

# browser.maximize_window()
time.sleep(2)
browser.find_element_by_name('username').send_keys('we_has_no_memes')
browser.find_element_by_name('password').send_keys('tuna1028')
browser.find_element_by_class_name('y3zKF').click()
time.sleep(3)
browser.get('https://www.instagram.com/shareking55/?hl=zh-tw')
# browser.find_element_by_class_name('HoLwm').click()
time.sleep(1)
# index = input('請輸入您要點第幾個文章')
browser.find_elements_by_class_name('_9AhH0')[0].click()

time.sleep(3)

browser.find_elements_by_class_name('sqdOP')[4].click()
# time.sleep(2)
exe_count = 1 # 紀錄執行次數
input('click to continue.')
while True:
    if exe_count == 1:
        input('click to continue.')

    if (exe_count%3) == 0:
        print('休息1分鐘')
        time.sleep(60)

    try:
        for j in range(2):
            # input('click to continue.')
            while True:
                targets  = browser.find_elements_by_class_name('y3zKF')
                if len(targets) > 9 or len(browser.find_elements_by_class_name('_8A5w5')) < 20:
                    break
                browser.find_elements_by_class_name('_8A5w5')[20].send_keys(Keys.PAGE_DOWN)
                browser.find_elements_by_class_name('_8A5w5')[20].send_keys(Keys.PAGE_DOWN)
                print('往下滾輪中...')
                time.sleep(2)

            for i in range(6,len(targets)-1):
                targets[i].click()
            # input('click to continue.')
            print('休息4秒')
            time.sleep(4)
            targets[6].send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            targets[6].send_keys(Keys.PAGE_DOWN)

        exe_count += 1
        print('分隔線....第'+ str(exe_count) +"次")
        time.sleep(1)#沒這個會出現element not interactable
    except Exception as e:
#================================我是分隔線================================
        error_class = e.__class__.__name__ #取得錯誤類型
        detail = e.args[0] #取得詳細內容
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
        fileName = lastCallStack[0] #取得發生的檔案名稱
        lineNum = lastCallStack[1] #取得發生的行號
        funcName = lastCallStack[2] #取得發生的函數名稱
        errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
        print(errMsg)
#================================我是分隔線================================
        print('發生例外')
        browser.close()
        #重開
        browser = webdriver.Chrome()
        #開啟google首頁
        browser.get('https://www.instagram.com/?hl=zh-tw')

        # browser.maximize_window()
        time.sleep(2)
        browser.find_element_by_name('username').send_keys('we_has_no_memes')
        browser.find_element_by_name('password').send_keys('tuna1028')
        browser.find_element_by_class_name('y3zKF').click()
        time.sleep(3)
        browser.get('https://www.instagram.com/shareking55/?hl=zh-tw')
        # browser.find_element_by_class_name('HoLwm').click()
        time.sleep(1)
        # index = input('請輸入您要點第幾個文章')
        browser.find_elements_by_class_name('_9AhH0')[0].click()
        time.sleep(3)

        browser.find_elements_by_class_name('sqdOP')[4].click()
        time.sleep(2)