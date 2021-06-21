'''
# @Title:
# @Time : 2021/6/17 17:19
# @File : add_department.py
# @Software: PyCharm

'''
from selenium.webdriver.common.by import By
from Page.BasePage import BasePage



class AddDepartmentPage(BasePage):

    def add_department(self,department_name):
        # circular_import问题-解决方案
        from Page.contact import ContactPage
        '''
        添加部门
        :return:
        '''
        self.find(By.CSS_SELECTOR,'.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR,'.js_create_party').click()
        self.find(By.NAME,'name').send_keys(department_name)
        self.find(By.CSS_SELECTOR, '.js_parent_party_name').click()
        self.find(By.CSS_SELECTOR,".qui_dialog_body.ww_dialog_body [id='1688851141767216_anchor']").click()
        self.find(By.LINK_TEXT,'确定').click()

        return ContactPage(self.driver)
