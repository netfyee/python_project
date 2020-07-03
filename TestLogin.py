#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def login(driver, user, password):
    driver.get('https://github.com/login')
    WebDriverWait(driver,5).until(EC.title_contains("Sign in to GitHub"))
    driver.find_element_by_name("login").send_keys(user)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("commit").click()
def check(driver):
    time.sleep(3)
    # 点右上角设置
    #driver.find_element_by_css_selector(".HeaderNavlink.name.mt-1").click()
    driver.find_element_by_xpath("html/body/div[1]/header/div[7]/details/summary").click()
    time.sleep(2)
    t = driver.find_element_by_xpath("html/body/div[1]/header/div[7]/details/details-menu/div[1]/a/strong").text
    print("获取到我的账户名称：%s" % t)

    if t == "netfyee":
        print("登录成功！")
        return True
    else:
        print("登录失败！")
        return False

def logout(driver):
    # 点sign out
    #driver.find_element_by_xpath("html/body/div[1]/header/div[7]/details/details-menu/form/button").click()
    driver.find_element_by_css_selector(".dropdown-item.dropdown-signout").click()
    driver.quit()

if __name__ == "__main__":
    profile_directory = r'C:\Users\netfy\AppData\Roaming\Mozilla\Firefox\Profiles\2ztcdm57.default-release'
    # 加载配置配置
    profile = webdriver.FirefoxProfile(profile_directory)
    # 启动浏览器配置
    browser = webdriver.Firefox(profile)
    browser.maximize_window()

    # 调用登录
    login(browser, "netfyee@hotmail.com", "fly2fyee")
    res = check(browser)
    if res:
        print("hello  netfyee!")
    # 调用退出
    logout(browser)