import logging
from multiprocessing.sharedctypes import Value
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sysName:str = os.path.dirname(__file__).replace("automation", "")
finalSysDir:str = os.path.join(sysName, 'data')
sys.path.append(finalSysDir)
import retrieveData

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


def goToStartMonth(monthName:str):
    actualMonth:webdriver = driver.find_element(by=By.CLASS_NAME, value="cmCalendarTitle").text
    while actualMonth.casefold() != monthName.casefold():
        time.sleep(0.8)
        driver.find_element(by=By.CLASS_NAME, value="previousMonth").click()
        actualMonth:webdriver = driver.find_element(by=By.CLASS_NAME, value="cmCalendarTitle").text

def goToNextMonth(monthName:str):
    actualMonth:webdriver = driver.find_element(by=By.CLASS_NAME, value="cmCalendarTitle").text
    while actualMonth.casefold() != monthName.casefold():
        time.sleep(0.8)
        driver.find_element(by=By.CLASS_NAME, value="nextMonth").click()
        actualMonth:webdriver = driver.find_element(by=By.CLASS_NAME, value="cmCalendarTitle").text
        


def testIteration():
    ciceronLoopSize:int = len(retrieveData.jsonExcelData())
    incrementLoopSize:int = 0
    goToStartMonth("MARZO DE 2022")
    while incrementLoopSize != ciceronLoopSize:    

        ciceronMonths:str = retrieveData.jsonExcelData()[incrementLoopSize]['Month']
        ciceronDays:str = retrieveData.jsonExcelData()[incrementLoopSize]['Day']
        ciceronHours:str = retrieveData.jsonExcelData()[incrementLoopSize]['Hours']
        ciceronDescription:str = retrieveData.jsonExcelData()[incrementLoopSize]['Description']
        ciceronOrientation:str = retrieveData.jsonExcelData()[incrementLoopSize]['Orientation']
        ciceronDifficulties:str = retrieveData.jsonExcelData()[incrementLoopSize]['Difficulties']
        ciceronObservations:str = retrieveData.jsonExcelData()[incrementLoopSize]['Observations']
        
        goToNextMonth(ciceronMonths)

        logging.debug("Finded Days")
        driver.find_element(by=By.CLASS_NAME, value=f"calendarDay{ciceronDays}.calendarDayWithFCT").click()
        logging.debug(f"Sending {ciceronDays}")

        logging.debug("Finded Hours")
        driver.find_element(by=By.ID, value="hours0").send_keys(ciceronHours)
        logging.debug(f"Sending {ciceronHours}")

        logging.debug("Finded Description")
        driver.find_element(by=By.ID, value="descr0").send_keys(ciceronDescription)
        logging.debug(f"Sending {ciceronDescription}")    

        logging.debug("Finded Orientation")
        driver.find_element(by=By.ID, value="directions0").send_keys(ciceronOrientation)
        logging.debug(f"Sending {ciceronOrientation}")

        logging.debug("Finded Difficulties")
        driver.find_element(by=By.ID, value="difficulties0").send_keys(ciceronDifficulties)
        logging.debug(f"Sending {ciceronDifficulties}")

        logging.debug("Finded Observations")
        driver.find_element(by=By.ID, value="comments0").send_keys(ciceronObservations)
        logging.debug(f"Sending {ciceronObservations}")    

        logging.debug("Finded Back Button")
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/form/div/input").click()

        incrementLoopSize+=1
        logging.debug("Loop incremented by 1")

def tempLoginCiceron(tempFileDir:str):
        time.sleep(sleepDeleteTempFiles)
        filesInDirectory:str = os.listdir(tempFileDir)
        filteredFiles:list = [file for file in filesInDirectory if file.endswith(".tmp")]
        print(filesInDirectory)
        for file in filteredFiles:
            pathFile:str = os.path.join(tempFileDir, file)
            os.remove(pathFile)
        driver.close()
