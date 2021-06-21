'''
# @Title:
# @Time : 2021/6/17 17:19
# @File : main.py
# @Software: PyCharm

'''
from selenium.webdriver.common.by import By

from Page.BasePage import BasePage
from Page.add_member import AddMemeberPage
from Page.contact import ContactPage


class MainPage(BasePage):

    def go_to_add_member(self):
        '''
        进入添加成员页面
        :return:
        '''
        self.driver.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMemeberPage(self.driver)

    def go_to_contact(self):
        '''
        进入通讯录
        :return:
        '''
        self.driver.find_element_by_link_text('通讯录').click()
        return ContactPage(self.driver)