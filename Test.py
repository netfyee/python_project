#coding=utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def SwitchFrame(driver,url):
    driver.get(url)
    driver.implicitly_wait(10.0)
    h = driver.current_window_handle
    print(h)
    driver.find_element_by_link_text("北京招聘").click()
    all_h = driver.window_handles
    print(all_h)
    #for x in all_h:
    #    if x != h :
    #        driver.switch_to_window(x)
    #        print(x.title())
    driver.switch_to_window(all_h[1])
    #print(driver.title)
    # 切换到首页句柄
    driver.close()
    driver.switch_to.window(h)
    print(driver.title)

def DealWindows(driver,url):
    driver.get(url)
    driver.implicitly_wait(10.0)
    h = driver.current_window_handle
    print(h)
    driver.find_element_by_link_text("北京招聘").click()
    all_h = driver.window_handles
    print(all_h)
    #for x in all_h:
    #    if x != h :
    #        driver.switch_to_window(x)
    #        print(x.title())
    driver.switch_to_window(all_h[1])
    #print(driver.title)
    # 切换到首页句柄
    driver.close()
    driver.switch_to.window(h)
    print(driver.title)

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

    SwitchFrame(browser,"http://bj.ganji.com/") #iFrame切换
    #DealWindows(browser, "http://bj.ganji.com/")  # 处理多窗口句柄

    #WebDriverWait(browser, 5).until(EC.title_contains(u"百度一下"))


    time.sleep(20.0)
    browser.quit()