from selenium import webdriver
from datetime import date

address = "https://www.y8.com"

driver = webdriver.Chrome()
driver.get(address)
containerElement = driver.find_element_by_id("items_container")
gameContainers = containerElement.find_elements_by_class_name("item")
gameLinks = []

for el in gameContainers:
    link = el.find_element_by_tag_name("a").get_attribute("href")
    gameLinks.append(link)

for link in gameLinks:
    driver.get(link)
    game_name = driver.find_element_by_tag_name("h1").text
    screenshot_name = "./site/y8.com/" + game_name + "_" + date.today().strftime("%Y-%m-%d") + ".png"
    driver.get_screenshot_as_file(screenshot_name)

driver.close()
