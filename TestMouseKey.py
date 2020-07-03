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
    mouse = browser.find_element_by_id("s-usersetting-top")
    ActionChains(browser).move_to_element(mouse).perform()
    #browser.find_element_by_id("kw").send_keys(Keys.ENTER)
    #context_click()
    #double_click()
    #send_keys(Keys.CONTROL, 'a')

    time.sleep(20.0)
    browser.quit()