#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time      : 2020/5/11 1:49 上午
# Software  : PyCharm
from time import sleep

from selenium import webdriver
class web:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def open_brower(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://172.20.10.5:8080/Shopping/')
        self.driver.implicitly_wait(10)
    def register(self):
        self.driver.find_element_by_css_selector('[href="fg-memberRegister.jsp"]').click()
        self.driver.find_element_by_name('name').send_keys('2')
        self.driver.find_element_by_name('password').send_keys('2')
        self.driver.find_element_by_name('passwordOne').send_keys('2')
        self.driver.find_element_by_name('reallyName').send_keys('2')
        self.driver.find_element_by_name('age').send_keys('2')
        self.driver.find_element_by_name('profession').send_keys('2')
        self.driver.find_element_by_name('email').send_keys('2')
        self.driver.find_element_by_name('question').send_keys('2')
        self.driver.find_element_by_name('result').send_keys('2')
        self.driver.find_element_by_css_selector('[class="input1"]').click()
        sleep(6)
    def login(self):
        self.driver.find_element_by_css_selector('[type="text"]').send_keys('2')
        self.driver.find_element_by_css_selector('[type="password"]').send_keys('2')
        self.driver.find_element_by_css_selector('[class="input1"]').click()
        sleep(3)
        data = self.driver.find_element_by_css_selector('tbody tr:nth-of-type(3) td[height="25"]').text
        return data
    def close(self):
        self.driver.close()
