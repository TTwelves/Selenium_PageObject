'''
# @Title:
# @Time : 2021/6/17 17:19
# @File : add_member.py
# @Software: PyCharm

'''
from selenium.webdriver.common.by import By

from Page.BasePage import BasePage
from Page.contact import ContactPage


class AddMemeberPage(BasePage):

    def AddMember(self,name,account,phone,email,job):
        '''
        添加成员
        :return:
        '''

        self.driver.implicitly_wait(5)
        self.find(By.ID,'username').send_keys(name)
        # 账号
        self.find(By.ID,'memberAdd_acctid').send_keys(account)
        # 手机号
        self.find(By.ID,'memberAdd_phone').send_keys(phone)
        # 邮箱
        self.find(By.ID,'memberAdd_mail').send_keys(email)
        # 职务
        self.find(By.ID,'memberAdd_title').send_keys(job)
        # 点击保存
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        # 注意不要写成ContactPage
        return ContactPage(self.driver)