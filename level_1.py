from selenium import webdriver
from datetime import date

address = "https://www.y8.com"

driver = webdriver.Chrome()
driver.get(address)
screenshot_name = "./site/y8.com/y8.com_" + date.today().strftime("%Y-%m-%d") + ".png"
driver.get_screenshot_as_file(screenshot_name)
driver.close()