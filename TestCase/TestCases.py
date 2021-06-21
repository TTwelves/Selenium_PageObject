'''
# @Title:
# @Time : 2021/6/17 17:24
# @File : TestCases.py
# @Software: PyCharm

'''
import pytest
import yaml
from Page.main import MainPage

# 读取成员信息文件
def get_member_datas():
    with open('member_data.yaml',encoding='UTF-8') as f:
        member_datas = yaml.safe_load(f)
    return member_datas

# 读取部门名称
def get_department_datas():
    with open('department_data.yaml',encoding='UTF-8') as f:
        department_data = yaml.safe_load(f)
    return department_data

class TestCases:

    @pytest.mark.parametrize('name,account,phone,email,job',get_member_datas())
    def test_add_member(self,name,account,phone,email,job):
        main = MainPage()
        # 1.进入添加成员页面 2.添加成员 3.返回通讯录，获取成员姓名
        namelist = main.go_to_add_member().AddMember(name,account,phone,email,job).get_name_list()
        # 断言判断
        assert name in namelist

    @pytest.mark.parametrize('department_name',get_department_datas())
    def test_add_department(self,department_name):
        main = MainPage()
        # 1.进入通讯录 2.进入添加部门页面 3.添加部门 4.返回通讯录,获取部门名称
        department_name_list = main.go_to_contact().go_to_add_department().add_department(department_name).get_department()
        assert department_name in department_name_list