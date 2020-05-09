from selenium import webdriver
from selenium.webdriver import Chrome
import time
driver = Chrome(executable_path="C:\\Driver\\chromedriver.exe")
url = "http://demo.automationtesting.in/Windows.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element_by_xpath("//div[@id='Tabbed']/a/button").click()
time.sleep(15)
currentwindow = driver.current_window_handle
allhandles = driver.window_handles
for handle in allhandles:
    if handle == currentwindow:
        continue
    driver.switch_to.window(handle)
    print(driver.title)
    driver.close()
    driver.switch_to.window(currentwindow)
    print(driver.title)