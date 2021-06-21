'''
# @Title:
# @Time : 2021/6/17 17:25
# @File : BasePage.py
# @Software: PyCharm

'''
import yaml
from selenium import webdriver


class BasePage:

    def find(self,by,ele=None):
        '''
        :param by: 定位方式：xpath css id
        :param ele:元素定位信息
        :return:
        '''
        if ele == None:
            #  * 的作用是解包
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by,ele)


    def __init__(self,base_driver = None):
        # 首次进入页面，创建一个新的driver
        if base_driver == None:
            self.driver = webdriver.Chrome()
            # 隐式等待,避免操作过快，页面来不及展开
            self.driver.implicitly_wait(5)
            # 最大化浏览器窗口
            self.driver.maximize_window()
            # 进入登录页
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
            # 读取cookie
            with open('../TestCase/cookies.yaml',encoding='UTF-8') as f:
                yaml_data = yaml.safe_load(f)
            # 装载cookie
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
            # 进入主页
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        else:
            # 复用同一个driver，使业务流程连贯
            self.driver = base_driver

