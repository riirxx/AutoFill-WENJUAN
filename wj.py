from selenium import webdriver
import random
import time
import datetime
import os

option = webdriver.ChromeOptions()
option.add_argument('headless')
url = 'www.wenjuan.com/xxx'
t = 1
today = datetime.datetime.now().strftime('%Y-%m-%d')
# 设置提交问卷次数
path = r"C:\chromedriver.exe"

for times in range(t):
    driver = webdriver.Chrome(executable_path=path, options=option)
    driver.get(url)
    # 定位所有的问卷问题
    questions = driver.find_elements_by_css_selector('.matrix')
    print(questions)
    for index,answers in enumerate(questions):

        # 定位所有问卷问题选项

        answer = answers.find_elements_by_css_selector('.icheckbox_div')
       
        if index == 0:
            js='document.getElementById("5e47b59e92beb51972fff0c5").removeAttribute("readonly")'
            driver.execute_script(js)
            blank_potion = answers.find_element_by_css_selector('.option')
            blank_potion.send_keys(today)
            time.sleep(4)
       
     

        elif index == 1:
            blank_potion = answers.find_element_by_css_selector('.blank')
            blank_potion.send_keys('XXX')
            time.sleep(4)
            subumit_button = driver.find_element_by_css_selector('#next_button')
            subumit_button.click()
            

    questions = driver.find_elements_by_css_selector('.matrix')
    print(questions)
    for index,answers in enumerate(questions):
        answer = answers.find_elements_by_css_selector('.icheckbox_div')
     
        if index == 2:
            blank_potion = answers.find_element_by_css_selector('.blank')
            blank_potion.send_keys('36.5')
            time.sleep(4)
   
        elif index == 3:
            choose_ans = answer[1]
            choose_ans.click()
            time.sleep(4)
        elif index == 4:
            choose_ans = answer[0]
            choose_ans.click()
            blank_potion = answers.find_element_by_css_selector('.option_open')
            blank_potion.send_keys('XXX')
            time.sleep(4)
        elif index == 5:
            choose_ans = answer[1]
            choose_ans.click()
            time.sleep(4)
    subumit_button = driver.find_element_by_css_selector('#next_button')
    subumit_button.click()
    print('已经成功提交了{}次问卷'.format(int(times) + int(1)))
    # 延迟问卷结果提交时间，以免间隔时间太短而无法提交
    time.sleep(7)
    driver.quit()


f = open('data.txt','a', encoding='utf-8')
f.write('\n')
f.writelines(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' 完成')
f.close()
