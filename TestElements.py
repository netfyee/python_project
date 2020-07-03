#coding=utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def GetDriver(profile):
    profile_directory = profile#r'C:\Users\netfy\AppData\Roaming\Mozilla\Firefox\Profiles\2ztcdm57.default-release'
    # 加载配置配置
    profile = webdriver.FirefoxProfile(profile_directory)
    # 启动浏览器配置
    browser = webdriver.Firefox(profile)
    browser.maximize_window()
    return browser

if __name__ == "__main__":
    browser = GetDriver(r'C:\Users\netfy\AppData\Roaming\Mozilla\Firefox\Profiles\2ztcdm57.default-release')
    browser.get("http://www.baidu.com")
    WebDriverWait(browser, 5).until(EC.title_contains(u"百度一下"))
    browser.find_element_by_id("kw").send_keys(u"测试部落")
    browser.find_element_by_id("kw").submit()
    WebDriverWait(browser, 5).until(EC.title_contains(u"测试部落"))
    #s = browser.find_elements_by_css_selector("h3.t>a")
    s = browser.find_elements_by_xpath(".//*[@id]/h3/a")
    print(s)
    for x in s:
        print(x.get_attribute("href"))

    # 设置随机值

    t = random.randint(0, 5)
    print(t)

    # 随机取一个结果点击鼠标

    s[t].click()
    time.sleep(20.0)
    browser.quit()