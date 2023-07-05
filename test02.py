import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


class TestCase02(unittest.TestCase):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://privoss.qiyuesuo.me/login")
    time.sleep(3)
    # def test_login_select(self):
    #
    #
    #     driver.find_element(By.XPATH,"//input[contains(@placeholder,'账号')]").send_keys("Qys_Admin")
    #     driver.find_element(By.XPATH, "//input[contains(@placeholder,'密码')]").send_keys("Qys_genyan@2022")
    #     driver.find_element(By.XPATH,"//*[@class='el-button el-button--primary']").click()
    #     time.sleep(3)
    #     parent_menu=driver.find_element(By.XPATH,"//*[text()='用户管理']").click()
    #     time.sleep(3)
    #     # 内部法人单位
    #     driver.find_element(By.XPATH, """//*[@id="app"]/div[2]/ul/li[2]/ul/li/ul/li[2]""").click()
    #     time.sleep(3)
    #     # 认证状态
    #     # sub_menu=driver.find_element(By.XPATH,"""//*[@id="app"]/div[3]/div/div[2]/div/div[1]/span[1]/div/div/input""").click()
    #     # sub_menu=driver.find_element(By.XPATH,"//*[text()='内部法人单位']").click()
    #     # 已认证
    #     # driver.find_element(By.XPATH, """/html/body/div[2]/div[1]/div[1]/ul/li[10]""").click()
    #     # driver.find_element(By.XPATH, """/html/body/div[2]/div[1]/div[1]/ul/li[1]/span""").click()
    #     # time.sleep(5)
    #     driver.find_element(By.XPATH,"""//*[@id="app"]/div[3]/div/div[2]/div/div[1]/span[1]/div/div/input""").click()
    #     time.sleep(3)
    #     driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[10]").click()
    #
    #     # sel.send_keys("已认证")
    #
    #
    #     time.sleep(100)
    #     # time.sleep(5)

    # def test_add_user(self):
    #     driver.find_element(By.XPATH, "//input[contains(@placeholder,'账号')]").send_keys("Qys_Admin")
    #     driver.find_element(By.XPATH, "//input[contains(@placeholder,'密码')]").send_keys("Qys_genyan@2022")
    #     driver.find_element(By.XPATH, "//*[@class='el-button el-button--primary']").click()
    #     time.sleep(3)
    #     #进入用户管理菜单
    #     driver.find_element(By.XPATH, "//*[text()='用户管理']").click()
    #     time.sleep(1)
    #     #找到个人用户管理菜单
    #     driver.find_element(By.XPATH,"""//*[@id="app"]/div[2]/ul/li[2]/ul/li/ul/li[4]""").click()
    #     time.sleep(3)
    #     #找到添加外部个人用户的入口,点击
    #     driver.find_element(By.XPATH,"""//*[@id="app"]/div[3]/div/div[1]/div/div[1]/a""").click()
    #     time.sleep(1)
    #     driver.find_element(By.XPATH,"""//*[@id="pane-manual"]/div[2]/form/div[1]/div/div/input""").send_keys("三十一")
    #     driver.find_element(By.XPATH,"""//*[@id="pane-manual"]/div[2]/form/div[2]/div/div/input""").send_keys("13000000011")
    #     #点击确定提交数据
    #     driver.find_element(By.XPATH,"""//*[@id="pane-manual"]/div[2]/div/button[1]/span""").click()


    def test_delete_user(self):
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'账号')]").send_keys("Qys_Admin")
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'密码')]").send_keys("Qys_genyan@2022")
        driver.find_element(By.XPATH, "//*[@class='el-button el-button--primary']").click()
        time.sleep(3)
        #进入用户管理菜单
        driver.find_element(By.XPATH, "//*[text()='用户管理']").click()
        time.sleep(1)
        #找到个人用户管理菜单
        driver.find_element(By.XPATH,"""//*[@id="app"]/div[2]/ul/li[2]/ul/li/ul/li[4]""").click()
        time.sleep(3)
        #找到认证状态筛选框
        driver.find_element(By.XPATH,"""//*[@id="app"]/div[3]/div/div[2]/div[1]/div[2]/div/div/input""").click()
        time.sleep(1)
        #搜索出状态未未认证的数据
        driver.find_element(By.XPATH,"""/html/body/div[7]/div[1]/div[1]/ul/li[1]/span""").send_keys("未认证")
        #获取未认证的列表数据
        page_data=driver.find_elements(By.XPATH,"//span[text()='更多']")
        if page_data:
            #找到第一行数据的更多按钮
            page_data[0].click()
            driver.find_element(By.XPATH,"""//*[@id="dropdown-menu-2065"]/li[3]/span/span""").click()
            time.sleep(3)
            ale=driver.switch_to.alert
            #弹窗点击确定
            ale.accept()




