import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/btm-fac/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(10)
cur_win_id = driver.current_window_handle
time.sleep(15)
driver.find_element_by_xpath("//span[text()='Login']").click()
mul_win_id=driver.window_handles
for id in mul_win_id:
    if(cur_win_id !=id):
        driver.switch_to.window(id)
        time.sleep(3)
        driver.find_element_by_id("inputEmail").send_keys("testt")
driver.close()
#driver.quit()

