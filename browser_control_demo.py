import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/btm-fac/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.makemytrip.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//a[text()='flights']").click()
driver.find_element_by_xpath("//a[text()='hotels']").click()
driver.back()
driver.forward()
#test