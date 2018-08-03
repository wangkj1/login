# -*- coding: UTF-8 -*-
'''
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginCase(unittest.TestCase):
   def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.maximize_window()

    #定义登录方法
   def login(self,username,password):
        self.dr.get("https://www.baidu.com")
        self.dr.find_element_by_xpath(".//*[@id='u1']/a[1]").click()
        self.dr.find_element_by_id("passLog").click()

        self.dr.find_element_by_id("TANGRAM__PSP_12__userName").clear()
        self.dr.find_element_by_id("TANGRAM__PSP_12__userName").send_keys(username)
        self.dr.find_element_by_id("TANGRAM__PSP_12__password").send_keys(password)
        self.dr.find_element_by_id("TANGRAM__PSP_12__submit").click()

   def test_login_sucess(self):   #用户名、密码正确
        self.login(u"a欺负狗的猫","wkj1230")   #正确的用户名和密码
        sleep(3)
        loginsucess = self.dr.find_element_by_xpath(".//*[@id='s_username_top']/span").text
        self.assertEqual(loginsucess,u"a欺负狗的猫")       #断言
        self.dr.get_screenshot_as_file("F:\login_sucess.jpg")   #截图

   def tearDown(self):
        sleep(2)
        print(u"测试结束")
        self.dr.quit()
if __name__ == '__main__':
    unittest.main()
'''





































