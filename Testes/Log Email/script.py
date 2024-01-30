from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium import webdriver 
import time, pyautogui

path = 'chromedriver.exe'
chrome_service = Service(path)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://www.google.com/intl/pt-BR/gmail/about/')

for a in range(0, 3):
    pyautogui.press('tab')
pyautogui.press('enter')

p1 = driver.find_element(By.ID, 'identifierId')
p1.send_keys('joaozinhoplays123@gmail.com') # Email genérico
pyautogui.press('enter')

time.sleep(960)

'Script não 100% funcional pois o google identifica que o sistema é automatizado'
