import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

path = 'chromedriver.exe'   
driver = webdriver.Chrome(service=Service(path))
driver.get('https://7b9405da61052ff7bd.gradio.live/')

promote = 'a cat in a shirt'

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="positive_prompt"]/label/textarea')))
input_promote = driver.find_element(By.XPATH, '//*[@id="positive_prompt"]/label/textarea')

input_promote.send_keys(promote)


WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="generate_button"]'))) 
generateclick = driver.find_element(By.XPATH, '//*[@id="generate_button"]')
generateclick.click()

time.sleep(100)










