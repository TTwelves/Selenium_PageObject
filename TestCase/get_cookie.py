'''
# @Title:
# @Time : 2021/6/17 17:26
# @File : get_cookie.py
# @Software: PyCharm

'''
import yaml
from selenium import webdriver

class TestGetCookie:
    def teardown(self):
        self.driver.quit()

    def test_get_cookie(self):
        '''
        使用浏览器复用的方式获取登录Cookie
        :return:
        '''
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        # 在复用浏览器进行操作
        self.driver.find_element_by_link_text('通讯录').click()
        cookies = self.driver.get_cookies()
        # 将cookie存入yaml文件
        with open('cookies.yaml','w',encoding='UTF-8') as f:
            yaml.dump(cookies,f)