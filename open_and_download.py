from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import time
import random
import datetime

username = input('Enter your username: ')
password = input('Enter your password: ')

download_limit = 50

chrome_path ="chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

def login():
    driver.get('https://pixabay.com/ru/accounts/login/?next=/')
    time.sleep(random.randint(2,4))

    username_elem = driver.find_element_by_xpath("//input[@name='username']")
    username_elem.clear()
    username_elem.send_keys(username)
    time.sleep(random.randint(2,4))

    password_elem = driver.find_element_by_xpath("//input[@name='password']")
    password_elem.clear()
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.ENTER)
    time.sleep(random.randint(2,4))

def download_pic(url_list,tot_downloads):
    count = 0
    number = tot_downloads
    remainder = len(url_list)-tot_downloads
    while remainder > 0:
        count += 1
        driver.get(url_list[number])
        number += 1
        time.sleep(random.randint(2,4))
        choose_size_button = driver.find_element_by_class_name("download_menu")
        choose_size_button.click()
        time.sleep(random.randint(2,4))
        max_size_button = driver.find_element_by_class_name('no_default')
        max_size_button.click()
        time.sleep(random.randint(2,4))
        download_button = driver.find_element_by_class_name('dl_btn')
        time.sleep(random.randint(2,4))
        download_button.click()
        time.sleep(random.randint(2,4))
        print('Downloading pic N%s' % count)

def url_list():
    with open ('Pixabay_pics_architecture.txt','r') as f:
        #f.seek(0)
        content = f.readlines()
        url_list = []
        for i in content:
            url = i.strip('\n')
            url_list.append(url)
        return url_list

def tot_downloads():     #returns the number of the downloaded pics
    a = len(os.listdir(path = r'C:\Users\Andrey\Desktop\PyProjects\PixabayParser\Downloaded'))
    b = len(os.listdir(path = r"C:\Users\Andrey\Desktop\PyProjects\InstaBot\Published"))
    return a + b

login()
download_pic(url_list(),tot_downloads())
