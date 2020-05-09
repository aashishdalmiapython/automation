from configparser import ConfigParser
from selenium.webdriver import Chrome
## import ActionChains & Keys class
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# fetching data from configuration file
objconfig=ConfigParser()
objconfig.read(".\\venv\\Config.cfg")
browser_exe_path = objconfig.get("Basics","path")


# created an object "driver" for chrome class
driver= Chrome(executable_path=browser_exe_path)
driver.get("https://www.thetestingworld.com/")
driver.maximize_window()

### Create object for action class
objaction=ActionChains(driver)

## left click anywhere
#objaction.click().perform()

## click on particular location
time.sleep(10)
#objaction.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

## right click anywere
#objaction.context_click().perform()

## double click
#objaction.double_click().perform()
#objaction.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

## Menu - mouse over & click on third level child.

objaction.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()
objaction.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]/parent::a/parent::li/div/div/div/div/ul/li/a/span[text()='FUNCTIONAL AUTOMATION']")).perform()
objaction.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]/parent::a/parent::li/div/div/div/div/ul/li/a/span[text()='FUNCTIONAL AUTOMATION']/parent::a/parent::li/div/div/div/div/ul/li/a/span[contains(text(), 'Selenium')]")).perform()
objaction.click(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]/parent::a/parent::li/div/div/div/div/ul/li/a/span[text()='FUNCTIONAL AUTOMATION']/parent::a/parent::li/div/div/div/div/ul/li/a/span[contains(text(), 'Selenium')]")).perform()

