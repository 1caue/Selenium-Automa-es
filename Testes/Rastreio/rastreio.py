from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium import webdriver 
import time, pyautogui

path = 'chromedriver.exe'
chrome_service = Service(path)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://www.linkcorreios.com.br/')
pyautogui.hotkey('win', 'up')

p1 = driver.find_element(By.NAME, 'id')
p1.send_keys('JN797275438BR')

p2 = driver.find_element(By.XPATH, '//*[@id="page"]/main/section/div/div[1]/form/div/div[2]/input')
p2.click()

time.sleep(7200)
