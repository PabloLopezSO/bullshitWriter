import logging
from multiprocessing.sharedctypes import Value
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

dirName:str = os.path.dirname(__file__)
finalDir:str = os.path.join(dirName, 'drivers/chrome/chromedriver.exe').replace('\\', '/')

sleepDeleteTempFiles = 3

logDir:str = os.path.dirname(__file__).replace('\\', '/').replace('/main/', '').replace('automation', '/')
finalLogDir:str = os.path.join(logDir, 'logs/automationLog/')


chromeDriverService:Service = Service(finalDir)
driver:webdriver = webdriver.Chrome(service=chromeDriverService)


def enterLoginCiceron():
    basicLoggingConf:logging = logging.basicConfig(filename=f"{finalLogDir}automatedLogin.log", filemode='w', level=logging.DEBUG, format='%(levelname)s:%(message)s')

    logging.debug("Started Driver")
    driver.get("https://ciceron-fct.educa.jcyl.es/ciceron/ciceron/tkMain?locale=es_ES")
    logging.debug("Maked connection with ciceron")
    driver.find_element(by=By.ID, value="dvLogin").send_keys("PabloLopez")
    logging.debug("Send user")
    driver.find_element(by=By.ID, value="dvPass").send_keys("Luispablo52")
    logging.debug("Send password")
    driver.find_element(by=By.CLASS_NAME, value="normal").click()
    logging.debug("Click and Login")

    open(f'{finalLogDir}\\login.tmp', 'a').close()
    

test = 1


def findDayCiceron():
    logging.debug("Finded Driver")
    driver.find_element(by=By.CLASS_NAME, value=f"calendarDay{test}.calendarDayWithFCT").click()

def findHoursCiceron():
    logging.debug("Finded Hours")
    driver.find_element(by=By.ID, value="hours0").send_keys("8")
    logging.debug("Sended 8 value")

def findDescriptionCiceron():
    logging.debug("Finded Description")
    driver.find_element(by=By.ID, value="descr0").send_keys("Description Goes Here")
    
def findOrientationCiceron():
    logging.debug("Finded Orientation")
    driver.find_element(by=By.ID, value="directions0").send_keys("Orientation Goes Here")

def findDifficultiesCiceron():
    logging.debug("Finded Difficulties")
    driver.find_element(by=By.ID, value="difficulties0").send_keys("Difficulties Goes Here")

def findObservationsCiceron():
    logging.debug("Finded Observations")
    driver.find_element(by=By.ID, value="comments0").send_keys("Observation Goes Here")
    
def findBackButton():
    logging.debug("Finded Back Button")
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/form/div/input").click()

def tempLoginCiceron(tempFileDir:str):
        time.sleep(sleepDeleteTempFiles)
        filesInDirectory = os.listdir(tempFileDir)
        filteredFiles = [file for file in filesInDirectory if file.endswith(".tmp")]
        print(filesInDirectory)
        for file in filteredFiles:
            pathFile = os.path.join(tempFileDir, file)
            os.remove(pathFile)
            
def dayLooper():
    logging.debug("Looping day")
    if test != 3:
        test += 1




