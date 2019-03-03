from selenium import webdriver
qspider=webdriver.Chrome(executable_path="C:/Users/btm-fac/Downloads/chromedriver_win32/chromedriver.exe")
qspider.get("file:///C:/Users/btm-fac/Desktop/qsp.html")
qspider.maximize_window()
qspider.implicitly_wait(30)
qspider.find_element_by_id("123").send_keys("admin")
qspider.find_element_by_id("123").send_keys("manager")
qspider.find_element_by_id("111").click()




qspider.find_element_by_xpath("")









