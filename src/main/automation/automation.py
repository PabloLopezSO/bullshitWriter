import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

dirName:str = os.path.dirname(__file__)
finalDir:str = os.path.join(dirName, 'drivers/chrome/chromedriver.exe').replace('\\', '/')
chromeDriverService = Service(finalDir)

print(finalDir)

driver = webdriver.Chrome(service=chromeDriverService)
driver.get("https://ciceron-fct.educa.jcyl.es/ciceron/ciceron/tkMain?locale=es_ES")
driver.find_element(by=By.ID, value="dvLogin").send_keys("PabloLopez")
driver.find_element(by=By.ID, value="dvPass").send_keys("Luispablo52")
driver.find_element(by=By.CLASS_NAME, value="normal").click()

""" 
driver.close() """



