#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


option = webdriver.ChromeOptions()
option.add_argument(r'--user-data-dir=C:\sers\netfy\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('disable-infobars')
#option.add_argument('--headless') #增加无界面选项
#option.add_argument('--disable-gpu') #关闭GPU模式，避免显示错误
browser=webdriver.Chrome(executable_path="C:\\Program Files\\Python35\\chromedriver.exe", chrome_options=option)
#browser.implicitly_wait(5) 
browser.get('http://www.huobi.me/')
browser.maximize_window()

title = EC.title_is(u'百度')
print(title(browser))
browser.find_element_by_name("total").send_keys("1111")


browser.find_element_by_id("kw").send_keys("111")
browser.find_element_by_name("wd").send_keys("222")
browser.find_element_by_class_name("s_ipt").send_keys("333")
browser.find_element_by_xpath(".//*[@id='kw']").send_keys("444")
browser.find_element_by_css_selector("#kw").send_keys("555")
#browser.find_element_by_tag_name("input").send_keys("666")
time.sleep(5.0)
WebDriverWait(browser,10).until(EC.title_is(u"百度一下，你就知道"))
browser.quit()
#browser.find_element_by_tag_name("input").send_keys("selenium")
#title = EC.title_is(u'百度')
#print(title(browser))
#print(EC.title_contains(u'百度')(browser))
#WebDriverWait(browser,10).until(EC.title_is(u"百度一下，你就知道"))
#browser.close()

profile_directory = r'C:\Users\netfy\AppData\Roaming\Mozilla\Firefox\Profiles\duo1ra95.default'
# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
browser = webdriver.Firefox(profile)
browser.get('http://www.baidu.com/')
browser.maximize_window()
browser.find_element_by_css_selector("#kw").send_keys("555")

'''
#########百度输入框的定位方式##########
#通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")
#通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")
#通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys("selenium")
#通过class name方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
#通过CSS方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
#通过xpath方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
############################################
browser.find_element_by_id("su").click()
'''