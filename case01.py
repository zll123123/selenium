from selenium import webdriver
import time


#打开浏览器
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#加载网页
from selenium.webdriver.common.keys import Keys
options = Options()
options.add_experimental_option('detach', True)
driver =  webdriver.Chrome()
driver.get("https://www.baidu.com")

#定位元素
#id定位
# element=driver.find_element(By.ID,"kw")
#name定位
# element=driver.find_element(By.NAME,"wd")
#xpath定位


# element=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[5]/div[1]/div/form/span[1]/input')
#相对路径+索引
# element=driver.find_element(By.XPATH,'//form/span[1]/input')

#相对路径+属性
# element=driver.find_element(By.XPATH,"//input[@autocomplete='off']")

#相对路径+通配符
# element=driver.find_element(By.XPATH,"//*[@*='off']")

#相对路径+部分属性值定位
#以什么开始
# element=driver.find_element(By.XPATH,"//*[starts-with(@autocomplete,'of')]")
#以什么结束
# element=driver.find_element(By.XPATH,"//*[substring(@autocomplete,2)='ff']")
#包含
# element=driver.find_element(By.XPATH,"//*[contains(@autocomplete,'of')]")


#相对路径+文本
element=driver.find_element(By.XPATH,"//span[text()='按图片搜索']")
print(element.get_attribute("class"))

#相对路径
#link_text定位
# element=driver.find_element(By.LINK_TEXT,"新闻")
if element:
    element.send_keys("李佳琦")
    element.send_keys(Keys.RETURN)
# if element:
#     element.click()
time.sleep(10)
