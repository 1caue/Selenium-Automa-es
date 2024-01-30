from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import time, pyautogui

path = 'chromedriver.exe'
chrome_service = Service(path)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://form.jotform.com/240175075976666')
pyautogui.hotkey('win', 'up')

time.sleep(10)
