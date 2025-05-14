from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time
PATH = 'chromedriver.exe'




driver = webdriver.Chrome(service=Service(PATH))
driver.get('https://www.google.com')

input_element = driver.find_element(By.ID,'APjFqb')
input_element.send_keys('Python')
input_element.clear()
input_element.send_keys('Pythonnew' + Keys.ENTER)

WebDriverWait(driver, 5 ).until(EC.presence_of_element_located((By.ID , 'APjFqb')))


link = driver.find_element(By.PARTIAL_LINK_TEXT, 'python.org')
link.click()
WebDriverWait(driver, 5 ).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT , 'python.org')))



time.sleep(1)
driver.quit()

