from configparser import ConfigParser
from selenium.webdriver import Chrome
# import ActionChains & Keys class
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


## fetching data from configuration file
objconfig=ConfigParser()
objconfig.read(".\\venv\\Config.cfg")
url = objconfig.get("Basics","url")
browser_exe_path = objconfig.get("Basics","path")


## created an object "driver" for chrome class
driver= Chrome(executable_path=browser_exe_path)
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath("//form[@name='register']/input[2]").send_keys("Aashish")

#####created object for action class to perform keyboard actions
objaction = ActionChains(driver)
objaction.key_down(Keys.CONTROL).send_keys("a").perform()
objaction.key_down(Keys.CONTROL).send_keys("c").perform()
driver.find_element_by_xpath("//form[@name='register']/input[3]").click()
objaction.key_down(Keys.CONTROL).send_keys("v").perform()