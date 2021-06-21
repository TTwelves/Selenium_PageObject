'''
# @Title:
# @Time : 2021/6/17 17:19
# @File : contact.py
# @Software: PyCharm

'''
from selenium.webdriver.common.by import By
from Page.BasePage import BasePage
from Page.add_department import AddDepartmentPage


class ContactPage(BasePage):

    def get_name_list(self):
        '''
        获取成员姓名
        :return:
        '''
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        nameList = []
        for ele in ele_list:
            nameList.append(ele.text)
        return nameList

    def go_to_add_department(self):
        '''
        进入添加部门页面
        :return:
        '''
        return  AddDepartmentPage(self.driver)

    def get_department(self):
        self.driver.refresh()
        self.driver.implicitly_wait(5)
        ele_list = self.driver.find_elements(By.CSS_SELECTOR,'.jstree-node.js_editable.jstree-leaf a')
        depart_list = []
        for ele in ele_list:
            depart_list.append(ele.text)
        print(depart_list)
        return depart_list