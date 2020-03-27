from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

exe_count = 0
while True:
    try:
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
        for j in range(2):
            input('click to continue.')
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
            time.sleep(4)
            targets[6].send_keys(Keys.PAGE_DOWN)

            targets[6].send_keys(Keys.PAGE_DOWN)
            print("休息1秒...")
            time.sleep(1)

        browser.close()
        exe_count += 1
        print('分隔線....第'+ str(exe_count) +"次")
    except:
        print('發生例外')
        browser.close()